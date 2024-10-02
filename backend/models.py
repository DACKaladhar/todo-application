from sqlalchemy import Column, Integer, String, Date, Time
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    created_date = Column(Date)
    created_time = Column(Time)
    updated_date = Column(Date, nullable=True)
    updated_time = Column(Time, nullable=True)
