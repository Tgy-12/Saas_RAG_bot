# Saas_RAG_bot
This is just Lets users sign up, log in and ask questions and to answer only via dUser Question
   ↓
Embed question
   ↓
FAISS similarity search
   ↓
Top-K relevant chunks
   ↓
Strict RAG prompt
   ↓
FLAN-T5 generates answer
ocumentation.

## **Phase** 6: Semantic Retrieval with FAISS

In this phase, we implemented semantic search over FAQ documents.

Steps:
1. Load FAISS index and metadata
2. Embed user query using SentenceTransformer
3. Perform similarity search using FAISS
4. Retrieve top-k relevant document chunks

This enables contextual retrieval for downstream LLM usage.

User Question
   ↓
Embed question
   ↓
FAISS similarity search
   ↓
Top-K relevant chunks
   ↓
Strict RAG prompt
   ↓
FLAN-T5 generates answer
