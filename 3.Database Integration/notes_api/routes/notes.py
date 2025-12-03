from fastapi import APIRouter, HTTPException, Query, Path
from typing import Optional
from schemas.notes import NoteCreate, NoteUpdate, NoteResponse, NoteListResponse
from services.notes_service import (
    create_note_service,
    get_all_notes_service,
    get_note_by_id_service,
    update_note_service,
    delete_note_service,
    search_notes_service
)

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=NoteResponse, status_code=201)
def create_note(note: NoteCreate):
    """
    Create a new note
    
    - **title**: Title of the note (required)
    - **content**: Content of the note (required)
    - **tags**: List of tags for categorization (optional)
    """
    try:
        return create_note_service(note)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating note: {str(e)}")


@router.get("/", response_model=NoteListResponse)
def get_all_notes(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of records to return"),
    tag: Optional[str] = Query(None, description="Filter by tag")
):
    """
    Retrieve all notes with optional pagination and filtering
    
    - **skip**: Number of records to skip (for pagination)
    - **limit**: Maximum number of records to return
    - **tag**: Filter notes by tag
    """
    try:
        return get_all_notes_service(skip=skip, limit=limit, tag=tag)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving notes: {str(e)}")


@router.get("/search", response_model=list[NoteResponse])
def search_notes(
    q: str = Query(..., min_length=1, description="Search term")
):
    """
    Search notes by title or content
    
    - **q**: Search term to look for in title and content
    """
    try:
        return search_notes_service(q)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching notes: {str(e)}")


@router.get("/{note_id}", response_model=NoteResponse)
def get_note_by_id(
    note_id: str = Path(..., description="Note ID")
):
    """
    Retrieve a specific note by ID
    
    - **note_id**: Unique identifier of the note
    """
    note = get_note_by_id_service(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: str = Path(..., description="Note ID"),
    note_data: NoteUpdate = None
):
    """
    Update an existing note
    
    - **note_id**: Unique identifier of the note
    - **title**: New title (optional)
    - **content**: New content (optional)
    - **tags**: New tags (optional)
    """
    updated_note = update_note_service(note_id, note_data)
    if not updated_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return updated_note


@router.delete("/{note_id}", status_code=204)
def delete_note(
    note_id: str = Path(..., description="Note ID")
):
    """
    Delete a note by ID
    
    - **note_id**: Unique identifier of the note
    """
    success = delete_note_service(note_id)
    if not success:
        raise HTTPException(status_code=404, detail="Note not found")
    return None
