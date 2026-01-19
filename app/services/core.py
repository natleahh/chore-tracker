"""Defines common service logic for querying SQLite databases."""

from sqlmodel import SQLModel, Session, select


class Service:
    def __init__(self, session: Session, table: type[SQLModel]) -> None:
        self._db: Session = session
        self._table: type[SQLModel] = table

    def read_all(self):
        return self._db.exec(select(self._table)).all()

    def read_by_pk(self, primary_key: int):
        return self._db.get(self._table, primary_key)

    def create(self, model: SQLModel):
        validated = self._table.model_validate(model)
        self._db.add(validated)
        self._db.commit()
        self._db.refresh(validated)
        return validated

    def delete(self, primary_key: int):
        model = self.read_by_pk(primary_key=primary_key)
        if model is None:
            return False
        self._db.delete(model)
        self._db.commit()
        return True
