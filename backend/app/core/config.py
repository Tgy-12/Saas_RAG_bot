'''from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
# from app.core.config import settings

SECRET_KEY = "your-secret-key-change-this"  # Move to .env later
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
'''
import os
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET", "dev_secret")
JWT_EXPIRES_MIN = int(os.getenv("JWT_EXPIRES_MIN", 60))
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
