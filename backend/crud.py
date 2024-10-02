from sqlalchemy.orm import Session
from datetime import date, time
import models

# Function to create a new todo
def create_todo(db: Session, text: str, created_date: date, created_time: time):
    new_todo = models.Todo(
        text=text,
        created_date=created_date,
        created_time=created_time
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Function to get all todos
def get_todos(db: Session):
    return db.query(models.Todo).all()

# Function to update an existing todo
def update_todo(db: Session, todo_id: int, text: str, updated_date: date, updated_time: time):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo:
        todo.text = text
        todo.updated_date = updated_date
        todo.updated_time = updated_time
        db.commit()
        db.refresh(todo)
        return todo
    return None

# Function to delete a todo
def delete_todo(db: Session, todo_id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
        return todo
    return None
