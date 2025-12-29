from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import router as auth_router
from app.api import rag
from app.db.session import Base, engine
from app.core.config import CORS_ORIGINS


app = FastAPI(title="SaaS RAG Support Copilot")

#DB tables are here
Base.metadata.create_all(bind=engine)

#cors settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Routers
app.include_router(auth_router, prefix="/auth")
app.include_router(rag.router)

@app.get("/health")
def health():
    return {"status": "ok"}
