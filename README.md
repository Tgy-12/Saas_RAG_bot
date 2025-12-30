# SaaS RAG Support Copilot — Week 1 Report

## Objective
Build a CPU-only Retrieval-Augmented Generation (RAG) backend using FastAPI and FAISS.
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


## Architecture
- FastAPI backend
- FAISS vector store
- SentenceTransformers embeddings
- FLAN-T5 (CPU-only)
- Chunk-based retrieval

## RAG Pipeline
1. Document chunking
2. Embedding generation
3. FAISS indexing
4. Similarity-based retrieval
5. Prompt construction
6. Guarded answer generation

## Guardrails
- Similarity threshold filtering
- Minimum chunk requirement
- Explicit refusal for low-context queries

## API Endpoints
- POST /rag/ask
- POST /auth/auth/signup
- POST /auth/auth/login
- GET /health

## Example Query
**Question:** What is Artificial Intelligence?  
**Status:** ok  
**Sources:** Returned from FAISS

## Out-of-Scope Handling
**Question:** Who is the CEO of Apple?  
**Status:** low_context  
**Answer:** Refusal (no hallucination)

## Constraints
- CPU-only
- Free models
- No external APIs

## Status
Week 1 completed successfully.


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
