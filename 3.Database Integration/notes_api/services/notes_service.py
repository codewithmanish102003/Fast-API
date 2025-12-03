from datetime import datetime
from bson import ObjectId
from typing import Optional
from database.mongodb import get_collection
from schemas.notes import NoteCreate, NoteUpdate, NoteResponse


# Collection name
NOTES_COLLECTION = "notes"


def serialize_note(note: dict) -> dict:
    """
    Convert MongoDB document to response format
    
    Args:
        note: MongoDB document
        
    Returns:
        Serialized note dictionary
    """
    if note:
        note["id"] = str(note["_id"])
        del note["_id"]
    return note


def create_note_service(note_data: NoteCreate) -> NoteResponse:
    """
    Create a new note in the database
    
    Args:
        note_data: Note creation data
        
    Returns:
        Created note response
    """
    collection = get_collection(NOTES_COLLECTION)
    
    # Prepare note document
    note_dict = note_data.model_dump()
    note_dict["created_at"] = datetime.utcnow()
    note_dict["updated_at"] = datetime.utcnow()
    
    # Insert into database
    result = collection.insert_one(note_dict)
    
    # Retrieve the created note
    created_note = collection.find_one({"_id": result.inserted_id})
    
    return NoteResponse(**serialize_note(created_note))


def get_all_notes_service(skip: int = 0, limit: int = 100, tag: Optional[str] = None) -> dict:
    """
    Retrieve all notes from the database with optional filtering
    
    Args:
        skip: Number of records to skip (for pagination)
        limit: Maximum number of records to return
        tag: Optional tag filter
        
    Returns:
        Dictionary containing list of notes and total count
    """
    collection = get_collection(NOTES_COLLECTION)
    
    # Build query filter
    query = {}
    if tag:
        query["tags"] = tag
    
    # Get total count
    total = collection.count_documents(query)
    
    # Retrieve notes with pagination
    notes_cursor = collection.find(query).skip(skip).limit(limit).sort("created_at", -1)
    notes = [NoteResponse(**serialize_note(note)) for note in notes_cursor]
    
    return {
        "notes": notes,
        "total": total
    }


def get_note_by_id_service(note_id: str) -> Optional[NoteResponse]:
    """
    Retrieve a single note by ID
    
    Args:
        note_id: Note ID
        
    Returns:
        Note response or None if not found
    """
    collection = get_collection(NOTES_COLLECTION)
    
    try:
        note = collection.find_one({"_id": ObjectId(note_id)})
        if note:
            return NoteResponse(**serialize_note(note))
        return None
    except Exception:
        return None


def update_note_service(note_id: str, note_data: NoteUpdate) -> Optional[NoteResponse]:
    """
    Update an existing note
    
    Args:
        note_id: Note ID
        note_data: Update data
        
    Returns:
        Updated note response or None if not found
    """
    collection = get_collection(NOTES_COLLECTION)
    
    try:
        # Prepare update data (only include non-None fields)
        update_dict = {k: v for k, v in note_data.model_dump().items() if v is not None}
        
        if not update_dict:
            # No fields to update
            return get_note_by_id_service(note_id)
        
        update_dict["updated_at"] = datetime.utcnow()
        
        # Update the note
        result = collection.find_one_and_update(
            {"_id": ObjectId(note_id)},
            {"$set": update_dict},
            return_document=True
        )
        
        if result:
            return NoteResponse(**serialize_note(result))
        return None
    except Exception:
        return None


def delete_note_service(note_id: str) -> bool:
    """
    Delete a note by ID
    
    Args:
        note_id: Note ID
        
    Returns:
        True if deleted, False otherwise
    """
    collection = get_collection(NOTES_COLLECTION)
    
    try:
        result = collection.delete_one({"_id": ObjectId(note_id)})
        return result.deleted_count > 0
    except Exception:
        return False


def search_notes_service(search_term: str) -> list[NoteResponse]:
    """
    Search notes by title or content
    
    Args:
        search_term: Search term
        
    Returns:
        List of matching notes
    """
    collection = get_collection(NOTES_COLLECTION)
    
    # Search in title and content using regex
    query = {
        "$or": [
            {"title": {"$regex": search_term, "$options": "i"}},
            {"content": {"$regex": search_term, "$options": "i"}}
        ]
    }
    
    notes_cursor = collection.find(query).sort("created_at", -1)
    notes = [NoteResponse(**serialize_note(note)) for note in notes_cursor]
    
    return notes
