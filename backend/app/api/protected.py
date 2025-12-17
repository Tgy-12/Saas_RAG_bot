from fastapi import APIRouter, Depends, HTTPException, status
from app.core.auth import verify_token

router = APIRouter(prefix="/users", tags=["users"])

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

@router.get("/me")
def get_current_user_info(current_user: dict = Depends(get_current_user)):
    return {"user_id": current_user.get("sub")}
