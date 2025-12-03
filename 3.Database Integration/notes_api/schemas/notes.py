from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class NoteBase(BaseModel):
    """Base schema for Note"""
    title: str = Field(..., min_length=1, max_length=200, description="Title of the note")
    content: str = Field(..., min_length=1, description="Content of the note")
    tags: Optional[list[str]] = Field(default=[], description="Tags for categorizing notes")


class NoteCreate(NoteBase):
    """Schema for creating a new note"""
    pass


class NoteUpdate(BaseModel):
    """Schema for updating an existing note"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=1)
    tags: Optional[list[str]] = None


class NoteResponse(NoteBase):
    """Schema for note response"""
    id: str = Field(..., description="Unique identifier for the note")
    created_at: datetime = Field(..., description="Timestamp when note was created")
    updated_at: datetime = Field(..., description="Timestamp when note was last updated")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "title": "My First Note",
                "content": "This is the content of my first note",
                "tags": ["personal", "important"],
                "created_at": "2024-12-04T01:00:00",
                "updated_at": "2024-12-04T01:00:00"
            }
        }


class NoteListResponse(BaseModel):
    """Schema for list of notes response"""
    notes: list[NoteResponse]
    total: int
