from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.users import UserCreate
from services.users_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(payload: UserCreate):
    return register_user(payload)

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    token = login_user(form.username, form.password)
    return {"access_token": token, "token_type": "bearer"}
