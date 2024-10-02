from http.client import HTTPException
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
import crud
from datetime import date, time
from pydantic import BaseModel

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TodoCreate(BaseModel):
    text: str
    created_date: date
    created_time: time

class TodoUpdate(BaseModel):
    text: str
    updated_date: date
    updated_time: time

@app.get("/todos/")
def read_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.post("/todos/")
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, text=todo.text, created_date=todo.created_date, created_time=todo.created_time)

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = crud.update_todo(
        db=db,
        todo_id=todo_id,
        text=todo.text,
        updated_date=todo.updated_date,
        updated_time=todo.updated_time
    )
    if updated_todo:
        return updated_todo
    return {"error": "Todo not found"}

# **Add the DELETE endpoint here**
@app.delete("/todos/{todo_id}")  # New DELETE endpoint
def delete_todo(todo_id: int, db: Session = Depends(get_db)):  # New delete function
    deleted_todo = crud.delete_todo(db, todo_id)
    if deleted_todo:
        return deleted_todo
    raise HTTPException(status_code=404, detail="Todo not found")  # Raise an exception if not found**