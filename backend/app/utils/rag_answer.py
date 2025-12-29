# Phase 6: RAG Answer Generation

import faiss
import pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# =========================
# Paths
# =========================
INDEX_DIR = Path("data/faiss")
INDEX_FILE = INDEX_DIR / "index.faiss"
META_FILE = INDEX_DIR / "metadata.pkl"

# =========================
# Load FAISS + metadata
# =========================
index = faiss.read_index(str(INDEX_FILE))

with open(META_FILE, "rb") as f:
    chunks = pickle.load(f)

# =========================
# Models (CPU only)
# =========================
embedder = SentenceTransformer("all-MiniLM-L6-v2")

qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    device=-1
)

# =========================
# Retrieval
# =========================
def retrieve_chunks(question: str, k: int = 4):
    """
    Retrieve top-k chunks from FAISS index with scores.
    Returns a list of dicts:
    {
        "content": str,
        "score": float,
        "faq_id": str,
        "title": str
    }
    """
    q_emb = embedder.encode([question]).astype("float32")
    distances, indices = index.search(q_emb, k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        if idx < 0 or idx >= len(chunks):
            continue  # skip invalid indices
        chunk = chunks[idx]
        results.append({
            "content": chunk.get("content", ""),
            "score": float(1 / (1 + dist)),  # convert distance to similarity score 0..1
            "faq_id": chunk.get("faq_id", f"unknown_{idx}"),
            "title": chunk.get("title", "Unknown Title")
        })
    return results


# =========================
# Prompt builder (TEXT ONLY)
# =========================
def build_prompt(question: str, context: str) -> str:
    return f"""
You are a helpful support assistant.
Answer ONLY using the information in the context below.
If the answer is not in the context, say:
"I do not have enough information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
""".strip()

# =========================
# Final RAG answer
# =========================
def answer_question(question: str) -> str:
    retrieved_chunks = retrieve_chunks(question)

    context = "\n".join(retrieved_chunks)

    prompt = build_prompt(question, context)

    output = qa_pipeline(
        prompt,
        max_new_tokens=200,
        do_sample=False
    )

    return output[0]["generated_text"]

# =========================
# CLI test
# =========================
if __name__ == "__main__":
    q = input("Ask a question: ")
    print("\nAnswer:\n")
    print(answer_question(q))

