from typing import Optional

from pydantic import BaseModel, Field
from utils.serializer import PyObjectId


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteInDB(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    content: str
    owner_id: PyObjectId

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}
