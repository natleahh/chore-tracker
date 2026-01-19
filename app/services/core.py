"""Defines common service logic for querying SQLite databases."""

from typing import Generic, TypeVar
from fastapi import HTTPException
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

    def read_by_pk(self, primary_key: int, raise_error: bool = False) -> SomeModel | None:
        """Reads row from primary key."""
        item = self._db.get(self._table, primary_key)
        if item is None and raise_error:
            raise HTTPException(
                status_code=404,
                detail=f"Item with primary key '{primary_key}' was not found in table {self._table}.",
            )
        return item

    def create(self, model: SomeModel) -> SomeModel:
        """Adds new row to base and return the validated result."""
        # validated = self._table.model_validate(model)
        self._db.add(model)
        self._db.commit()
        self._db.refresh(model)
        return model

    def delete(self, primary_key: int) -> bool:
        """Removes row from base from on primary key."""
        model = self.read_by_pk(primary_key=primary_key)
        if model is None:
            return False
        self._db.delete(model)
        self._db.commit()
        return True
