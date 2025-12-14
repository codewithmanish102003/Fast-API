from typing import List

from core.database import connect
from pymongo.collection import Collection
from schemas.notes import NoteCreate


def get_notes_collection() -> Collection:
    db = connect()
    return db.get_collection("notes")


def create_note(note: NoteCreate, owner_id: str) -> dict:
    notes = get_notes_collection()
    doc = {"title": note.title, "content": note.content, "owner_id": owner_id}
    res = notes.insert_one(doc)
    return notes.find_one({"_id": res.inserted_id})


def get_notes_for_user(user_id: str) -> List[dict]:
    notes = get_notes_collection()
    return list(notes.find({"owner_id": user_id}))


def get_note_by_id(note_id: str) -> dict:
    notes = get_notes_collection()
    from bson import ObjectId

    return notes.find_one({"_id": ObjectId(note_id)})


def delete_note(note_id: str):
    notes = get_notes_collection()
    from bson import ObjectId

    return notes.delete_one({"_id": ObjectId(note_id)})
