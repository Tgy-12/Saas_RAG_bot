from fastapi import APIRouter
from pydantic import BaseModel
from app.utils import retrieve_faqs, rag_answer
import uuid

SIMILARITY_THRESHOLD = 0.75
MIN_CHUNKS_REQUIRED = 1

router = APIRouter()

class AskRequest(BaseModel):
    question: str

class SourceChunk(BaseModel):
    chunk_text: str
    score: float
    doc_id: str
    title: str
    chunk_id: str

class AskResponse(BaseModel):
    answer: str
    sources: list[SourceChunk]
    status: str
    trace_id: str


@router.post("/rag/ask", response_model=AskResponse)
def ask_rag(req: AskRequest):
    trace_id = str(uuid.uuid4())

    # Retrieve top chunks
    all_chunks = retrieve_faqs.retrieve_faqs(req.question)

    good_chunks = [
        c for c in all_chunks
        if c.get("score", 0) >= SIMILARITY_THRESHOLD
    ]


    # Check if we have any chunks above threshold

    if len(good_chunks) < MIN_CHUNKS_REQUIRED:
        return AskResponse(
            answer="I do not have enough information in the provided documents...",
            sources=[],
            status="low_context",
            trace_id=trace_id
        )

    # Build context from chunks
    context = "\n\n".join([c["content"] for c in good_chunks if "content" in c])

    # Build the prompt
    prompt = rag_answer.build_prompt(req.question, context)

    # Generate answer using the pipeline
    output = rag_answer.qa_pipeline(
        prompt,
        max_new_tokens=200,
        do_sample=False
    )

    answer_text = output[0]["generated_text"].strip() if output else "I do not have enough information in the provided documents."

    # Build sources
    sources = [
        SourceChunk(
            chunk_text=c["content"],
            score=float(c.get("score", 0)),
            doc_id=c.get("faq_id", ""),
            title=c.get("title", ""),
            chunk_id=f"{c.get('faq_id', 'unknown')}_{i}",
        )
        for i, c in enumerate(good_chunks)
    ]

    print(f"[RAG] trace_id={trace_id} question={req.question}")
    print(f"[RAG] chunks_used={len(good_chunks)}")

    return AskResponse(
        answer=answer_text,
        sources=sources,
        status="ok",
        trace_id=trace_id
)
