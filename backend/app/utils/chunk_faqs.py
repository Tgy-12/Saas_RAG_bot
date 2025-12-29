#phase_2: chunking of the ingested faq in to smaller doc chunks and use langachain_text_spliter for chunking
import json
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_FILE = Path("data/docs.json")

def load_faqs():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def chunk_faqs(faqs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,#this parameter defines the maximum size of each chunk of text. In this case, each chunk will be at most 400 characters long.and the generated chunks will not exceed this length.but when we make this length to 500 or 600 the model performance may decrease as the chunks become too large to process effectively.on the other hand if we set this length to a very small value like 100 or 150 the model performance may also decrease as the chunks become too small to provide sufficient context for understanding the content.so 400 is a balanced choice for chunk size.the greater the chunk size the fewer chunks will be generated from the same text as a result larger chunks may be harder for models to process effectively.
        chunk_overlap=50,#chunk_overlap determines how much overlap there is between chunks of text. This can be useful for maintaining context across chunks.the same piece of information appears in multiple chunks, making it easier for models to understand the context when processing each chunk individually.and in this case the number of overlap of 50 character implies that each chunk will share 50 characters with the previous chunk.
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = []

    for faq in faqs:
        text = f"{faq['title']}\n\n{faq['body']}"
        split_texts = splitter.split_text(text)

        for i, chunk in enumerate(split_texts):
            chunks.append({
                "faq_id": faq["id"],
                "title": faq["title"],
                "chunk_index": i,
                "content": chunk
            })

    return chunks


if __name__ == "__main__":
    faqs = load_faqs()
    chunks = chunk_faqs(faqs)

    print(f"Original FAQs: {len(faqs)}")
    print(f"Generated chunks: {len(chunks)}")

    print("\nSample chunk:")
    print(chunks[:4])
