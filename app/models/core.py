"""Defines underlying data structures of database models."""

from sqlmodel import SQLModel


class Chore(SQLModel):
    """Chore base model."""

    name: str
    description: str | None = None
