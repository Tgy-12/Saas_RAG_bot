#This is all about the sample documentation.

#the RAG pipe line had the following procedures

```steps
1,**Ingestion**: to read docs
2,**chunkings**: split in to small pices.
3.**Embeddings**: convert each chunk in to vector
4.**: save the vector to db FAISS/chroma
5. **Retrive**: find top-k similar chunks for a question
6.**prompt**: sends chunk + question LLM
7.**Answer**:return generateed answer +sources
```

