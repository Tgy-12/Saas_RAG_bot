#phase_3: embeding for the chunked files by changing to numbers vectors wiith sentence transformer
import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
#from .chunk_faqs import chunks

DATA_FILE = Path("data/docs.json")

def load_faqs():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def chunk_faqs(faqs):
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

    chunks = []
    for faq in faqs:
        text = f"{faq['title']}\n\n{faq['body']}"
        split_texts = splitter.split_text(text)

        for i, chunk in enumerate(split_texts):
            chunks.append({
                "faq_id": faq["id"],
                "title": faq["title"],
                "content": chunk
            })

    return chunks


if __name__ == "__main__":
    print("Loading model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    faqs = load_faqs()
    chunks = chunk_faqs(faqs)

    texts = [c["content"] for c in chunks]

    print(f"Embedding {len(texts)} chunks...")
    embeddings = model.encode(texts, show_progress_bar=True)

    print("Embedding shape:")
    print(embeddings.shape)

    print("\nSample vector (first 10 values):")
    print(embeddings[0][:10])
    print("\nSample chunk content:")
#yields 384 = correct dimension for MiniLM
