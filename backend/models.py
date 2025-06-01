from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    docs_url: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Certificate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int
    organization_id: int
    course_name: str
    hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
