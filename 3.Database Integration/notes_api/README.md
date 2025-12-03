# Notes API with MongoDB Integration

A complete RESTful API for managing notes built with FastAPI and MongoDB.

## 📁 Project Structure

```
notes_api/
│
├── main.py                 # FastAPI application entry point
│
├── database/
│   └── mongodb.py         # MongoDB connection and configuration
│
├── schemas/
│   └── notes.py           # Pydantic models for request/response
│
├── routes/
│   └── notes.py           # API endpoints
│
└── services/
    └── notes_service.py   # Business logic and database operations
```

## 🚀 Features

- ✅ Create, Read, Update, Delete (CRUD) operations for notes
- ✅ Search notes by title or content
- ✅ Filter notes by tags
- ✅ Pagination support
- ✅ MongoDB integration
- ✅ Input validation with Pydantic
- ✅ Comprehensive API documentation (Swagger UI)

## 📋 Prerequisites

- Python 3.8+
- MongoDB (running locally on port 27017)

## 🛠️ Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Make sure MongoDB is running:**
   ```bash
   # On Windows (if MongoDB is installed as a service)
   net start MongoDB
   
   # Or run MongoDB manually
   mongod
   ```

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

## 📚 API Documentation

Once the server is running, visit:
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 🔌 API Endpoints

### Notes

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/notes/` | Create a new note |
| GET | `/notes/` | Get all notes (with pagination) |
| GET | `/notes/{note_id}` | Get a specific note by ID |
| PUT | `/notes/{note_id}` | Update a note |
| DELETE | `/notes/{note_id}` | Delete a note |
| GET | `/notes/search?q=term` | Search notes by title/content |

### Example Requests

**Create a Note:**
```bash
curl -X POST "http://127.0.0.1:8000/notes/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Note",
    "content": "This is the content of my note",
    "tags": ["personal", "important"]
  }'
```

**Get All Notes:**
```bash
curl "http://127.0.0.1:8000/notes/?skip=0&limit=10"
```

**Search Notes:**
```bash
curl "http://127.0.0.1:8000/notes/search?q=first"
```

**Update a Note:**
```bash
curl -X PUT "http://127.0.0.1:8000/notes/{note_id}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "content": "Updated content"
  }'
```

**Delete a Note:**
```bash
curl -X DELETE "http://127.0.0.1:8000/notes/{note_id}"
```

## 🗄️ Database Configuration

The MongoDB connection settings can be modified in `database/mongodb.py`:

```python
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "notes_db"
```

## 📝 Note Schema

```json
{
  "title": "string (required, max 200 chars)",
  "content": "string (required)",
  "tags": ["array of strings (optional)"],
  "created_at": "datetime (auto-generated)",
  "updated_at": "datetime (auto-generated)"
}
```

## 🧪 Testing the API

You can test the API using:
- The interactive Swagger UI at `/docs`
- Tools like Postman or Insomnia
- cURL commands (examples above)
- Python requests library

## 🔧 Configuration

### MongoDB Connection
Edit `database/mongodb.py` to change:
- MongoDB URI
- Database name
- Connection settings

### API Settings
Edit `main.py` to customize:
- API title and description
- Version
- Additional middleware
- CORS settings (if needed)

## 📦 Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI
- **PyMongo**: MongoDB driver for Python
- **Pydantic**: Data validation using Python type annotations

## 🎯 Next Steps

Consider adding:
- User authentication (JWT)
- Rate limiting
- Caching (Redis)
- File attachments for notes
- Categories/folders for organizing notes
- Sharing notes with other users
- Rich text formatting support
