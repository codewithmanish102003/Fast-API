from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from utils.serializer import PyObjectId


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    role: str = "user"


class UserInDB(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    hashed_password: str
    full_name: Optional[str] = None
    role: str = "user"

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}


class UserPublic(BaseModel):
    id: PyObjectId = Field(alias="_id")
    email: EmailStr
    full_name: Optional[str] = None
    role: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[str] = None
    role: Optional[str] = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    user: UserPublic
    token: Token
