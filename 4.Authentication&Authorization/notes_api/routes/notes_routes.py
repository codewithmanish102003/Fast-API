from fastapi import APIRouter, Depends
from bson import ObjectId
from core.database import notes_collection
from dependencies.auth import get_current_user, require_admin
from schemas.notes import NoteCreate, NoteUpdate

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/")
def create_note(payload: NoteCreate, user=Depends(get_current_user)):
    note = {**payload.dict(), "user_id": user["id"]}
    notes_collection.insert_one(note)
    return {"message": "Note created"}

@router.get("/")
def get_notes(user=Depends(get_current_user)):
    return list(notes_collection.find({"user_id": user["id"]}, {"_id": 0}))

@router.delete("/{note_id}")
def delete_note(note_id: str, admin=Depends(require_admin)):
    notes_collection.delete_one({"_id": ObjectId(note_id)})
    return {"message": "Note deleted"}
