from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

#HTTP Methods
@app.post("/")
def create():
    return {"message": "Post request"}  

@app.put("/")
def update():
    return {"message": "Put request"}

@app.delete("/")
def delete():
    return {"message": "Delete request"}

@app.get("/")
def read():
    return {"message": "Get request"}

    