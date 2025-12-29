#phase_1: ingesting part of RAG mean to analyze which is to be chunked
import json
from pathlib import Path

DATA_PATH = Path("data")

def load_faqs():
    faqs = []

    for file in DATA_PATH.glob("*.json"):#glob is a methode use to iterate over the subtree and yields all the possible files with in that path.
        with open(file, "r", encoding="utf-8") as f:
            content = json.load(f)
            if isinstance(content, list):
                faqs.extend(content)
            else:
                faqs.append(content)
    return faqs

if __name__ == "__main__":
    faqs = load_faqs()
    print(f"{len(faqs)} FAQ of documents are loaded.")

    for faq in faqs[:3]:  # Print first 3 FAQs as a sample
        print(json.dumps(faq, indent=2))
