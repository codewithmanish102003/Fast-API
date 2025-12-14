from fastapi import APIRouter, Depends, HTTPException
from schemas.users import UserCreate, UserPublic, Token, LoginRequest, LoginResponse
from services.users import authenticate_user, create_tokens_for_user, create_user
from dependencies.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=UserPublic)
def register(user: UserCreate):
    try:
        created = create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return created


@router.get("/me", response_model=UserPublic)
def me(user=Depends(get_current_user)):
    """Get current user information"""
    user["_id"] = str(user["_id"])
    return user


@router.post("/login", response_model=LoginResponse, summary="Login to get access token", name="login")
def login(credentials: LoginRequest):
    """Login endpoint to authenticate users and get access token with user data"""
    user = authenticate_user(credentials.email, credentials.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token_data = create_tokens_for_user(user)
    token = Token(access_token=token_data["access_token"], token_type=token_data["token_type"])
    user_public = UserPublic(
        _id=user["_id"],
        email=user["email"],
        full_name=user.get("full_name"),
        role=user["role"]
    )
    return LoginResponse(user=user_public, token=token)

@router.post("/create-admin")
def create_admin(secret: str):
    from core.config import settings

    if secret != settings.admin_secret:
        raise HTTPException(status_code=403, detail="Invalid admin secret")
    admin = UserCreate(email="admin@example.com", password="adminpass", role="admin")
    try:
        created = create_user(admin)
    except ValueError:
        raise HTTPException(status_code=400, detail="Admin already exists")
    created["_id"] = str(created["_id"])
    return created
