#phase_5: real building of faiss index from the embedded vectors. this will allow for efficient similarity search and retrieval of relevant chunks based on user queries.from embed_faqs.py we will import the embedded vectors and then build the faiss index.
import json
from pathlib import Path
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import numpy as np
#from typing import cast

DATA_FILE = Path("data/docs.json")
INDEX_DIR = Path("data/faiss")
INDEX_DIR.mkdir(exist_ok=True)

def load_faqs():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def chunk_faqs(faqs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )
    chunks = []
    for faq in faqs:
        text = f"{faq['title']}\n\n{faq['body']}"
        for i, chunk in enumerate(splitter.split_text(text)):
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

    print("Creating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")
    embeddings = np.ascontiguousarray(embeddings)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings) #type: ignore[arg-type]

    print(f"FAISS index size: {index.ntotal}")

    # Save indexP
    faiss.write_index(index, str(INDEX_DIR / "index.faiss"))

    # Save metadata
    with open(INDEX_DIR / "metadata.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("FAISS index and metadata saved.")
