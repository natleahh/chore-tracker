"""Defines logic for querying or adding information to the SQLite database."""

from datetime import datetime
from sqlmodel import Session

from app.db import tables
from app.services import core


class Chore(core.Service):
    """Chore service."""

    def __init__(self, session: Session) -> None:
        """Initialises chore service."""
        super().__init__(session=session, table=tables.Chore)


class Completion(core.Service):
    """Chore completion service."""

    def __init__(self, session: Session) -> None:
        """Initialises Completion service."""
        super().__init__(session, table=tables.Completion)

    def complete_chore(self, time: datetime, chore: tables.Chore | None):
        """Complete chore at specified time."""
        if chore is None:
            raise ValueError('Chore is None.')
        completion = self._table(time=time, chore=chore, chore_id=chore.id)
        return self.create(completion)

    def complete_chore_now(self, chore: tables.Chore):
        """Complete Chore at current time."""
        return self.complete_chore(time=datetime.now(), chore=chore)
