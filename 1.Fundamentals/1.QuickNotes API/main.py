from fastapi import FastAPI, HTTPException
from models import Note, NoteResponse

app = FastAPI()

notes_db = []   # in-memory store
current_id = 1  # simple incremental ID


@app.get("/")
def home():
    return {"message": "QuickNotes API Running"}


@app.post("/notes", response_model=NoteResponse)
def create_note(note: Note):
    global current_id
    new_note = {"id": current_id, **note.dict()}
    notes_db.append(new_note)
    current_id += 1
    return new_note


@app.get("/notes", response_model=list[NoteResponse])
def get_notes(limit: int = 10):
    return notes_db[:limit]


@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note_by_id(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    for note in notes_db:
        if note["id"] == note_id:
            notes_db.remove(note)
            return {"message": "Note deleted"}
    raise HTTPException(status_code=404, detail="Note not found")
