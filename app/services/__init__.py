"""Defines logic for querying or adding information to the SQLite database"""

from sqlmodel import Session

from app.db import tables
from app.services import core


class Chore(core.Service):
    def __init__(self, session: Session) -> None:
        super().__init__(session=session, table=tables.Chore)
