from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, protected
from app.database import engine
from app.models import user as user_models

# Create tables
user_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="SaaS Copilot API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(protected.router)

@app.get("/")
def read_root():
    return {"message": "SaaS Copilot API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
