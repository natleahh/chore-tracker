"""Defined database tables and underling relationships."""

from sqlmodel import Field, Relationship

from app.models import core


class Chore(core.Chore, table=True):
    """Chore database table."""

    id: int | None = Field(default=None, primary_key=True)
    completions: list['Completion'] = Relationship(back_populates='chore')


class Completion(core.Completion, table=True):
    """Chore completion database table."""

    id: int | None = Field(default=None, primary_key=True)
    chore: Chore = Relationship(back_populates='completions')
