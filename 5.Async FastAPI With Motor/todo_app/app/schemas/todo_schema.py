from pydantic import BaseModel, Field
from typing import Optional

class TodoCreate(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    completed: bool