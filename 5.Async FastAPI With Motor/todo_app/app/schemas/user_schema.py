from pydantic import BaseModel , EmailStr, Field

class UserRegister(BaseModel):
    email:EmailStr=Field(...)
    password:str=Field(min_length=6,max_length=12)

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:str
    email:EmailStr