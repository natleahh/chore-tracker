"""Defines underlying data structures of database models."""

from sqlmodel import SQLModel


class Chore(SQLModel):
    name: str
    description: str | None = None
