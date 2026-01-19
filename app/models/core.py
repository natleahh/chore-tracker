"""Defines underlying data structures of database models."""

from datetime import datetime
from sqlmodel import Field, SQLModel


class Chore(SQLModel):
    """Chore base model."""

    name: str
    description: str | None = None


class Completion(SQLModel):
    """Chore completion model."""

    time: datetime
    chore_id: int = Field(foreign_key='chore.id')
