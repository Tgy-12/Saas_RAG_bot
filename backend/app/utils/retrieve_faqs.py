#phase_6: retrieval of faqs using the built faiss index. this will involve loading the index and performing similarity search based on user queries to fetch relevant faq chunks.
import faiss
import pickle
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_DIR = Path("data/faiss")
INDEX_FILE = INDEX_DIR / "index.faiss"
METADATA_FILE = INDEX_DIR / "metadata.pkl"

TOP_K = 5  # Number of top similar faqs to retrieve

def load_index():
    index = faiss.read_index(str(INDEX_FILE))
    with open(METADATA_FILE, "rb") as f:
        metadata = pickle.load(f)
    return index, metadata

def embed_query(query: str, model):
    vector = model.encode([query])
    return np.array(vector).astype("float32")

def retrieve_faqs(query: str):
    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    index, metadata = load_index()
    query_vector = embed_query(query, model)

    distances, indices = index.search(query_vector, TOP_K)

    results = []
    for idx in indices[0]:
        if idx != -1:#idx == -1 means no more results
            results.append(metadata[idx])
    return results

if __name__ == "__main__":
    question = "what is the difference between AI and machine learning?"
    results = retrieve_faqs(question)

    print("\nTop FAQ Results:\n")
    for i, r in enumerate(results, 1):
        print(f"{i}. {r['content'][:200]}...\n")
