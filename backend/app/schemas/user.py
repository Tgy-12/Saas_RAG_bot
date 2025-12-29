from pydantic import BaseModel, EmailStr
class UserCreate(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    password: str
class UserLogin(BaseModel):
    username: str
    password: str
class UserOut(BaseModel):
    id: int
    full_name: str
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
