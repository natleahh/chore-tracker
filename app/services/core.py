"""Defines common service logic for querying SQLite databases."""

from typing import Generic, TypeVar
from sqlmodel import SQLModel, Sequence, Session, select

SomeModel = TypeVar('SomeModel', bound=SQLModel)


class Service(Generic[SomeModel]):
    """Servce Base Class."""

    def __init__(self, session: Session, table: type[SomeModel]) -> None:
        """Initialises Service instance."""
        self._db: Session = session
        self._table: type[SomeModel] = table

    def read_all(self) -> Sequence[SomeModel]:
        """Reads all rows from table."""
        return self._db.exec(select(self._table)).all()  # mypy: noqa

    def read_by_pk(self, primary_key: int) -> SomeModel | None:
        """Reads row from primary key."""
        return self._db.get(self._table, primary_key)

    def create(self, model: SomeModel) -> SomeModel:
        """Adds new row to base and return the validated result."""
        validated = self._table.model_validate(model)
        self._db.add(validated)
        self._db.commit()
        self._db.refresh(validated)
        return validated

    def delete(self, primary_key: int) -> bool:
        """Removes row from base from on primary key."""
        model = self.read_by_pk(primary_key=primary_key)
        if model is None:
            return False
        self._db.delete(model)
        self._db.commit()
        return True
