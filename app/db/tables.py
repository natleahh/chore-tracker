"""Defined database tables and underling relationships."""

from sqlmodel import Field

from app.models import core


class Chore(core.Chore, table=True):
    """Chore database table."""

    id: int | None = Field(default=None, primary_key=True)
