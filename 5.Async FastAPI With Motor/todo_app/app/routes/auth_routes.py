from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserRegister, UserLogin
from app.services.user_service import register_user, login_user

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/register")
async def register(data: UserRegister):
    user_id = await register_user(data.email, data.password)
    if not user_id:
        raise HTTPException(status_code=400, detail="User already exists")

    return {"message": "User registered successfully"}

@router.post("/login")
async def login(data: UserLogin):
    token = await login_user(data.email, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token, "token_type": "bearer"}
