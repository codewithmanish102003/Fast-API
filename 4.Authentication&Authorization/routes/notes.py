from dependencies.auth import get_current_user, require_role
from fastapi import APIRouter, Depends, HTTPException
from schemas.notes import NoteCreate
from services.notes import (create_note, delete_note, get_note_by_id,
                            get_notes_for_user)

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("/", summary="Create a note")
def create(note: NoteCreate, user=Depends(get_current_user)):
    created = create_note(note, str(user.get("_id")))
    return created


@router.get("/", summary="List my notes")
def list_notes(user=Depends(get_current_user)):
    return get_notes_for_user(str(user.get("_id")))


@router.get("/{note_id}")
def get_note(note_id: str, user=Depends(get_current_user)):
    n = get_note_by_id(note_id)
    if not n:
        raise HTTPException(status_code=404, detail="Note not found")
    if n.get("owner_id") != str(user.get("_id")) and user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not allowed")
    return n


@router.delete("/{note_id}")
def remove(note_id: str, user=Depends(require_role("admin"))):
    res = delete_note(note_id)
    return {"deleted_count": res.deleted_count}
