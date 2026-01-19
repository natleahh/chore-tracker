"""Contains code for interacting with the SQLite database and initiating sessions."""

from typing import Annotated

from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine

from app.core.config import config

from . import tables

__all__ = ['tables', 'engine', 'SessionDep']


engine = create_engine(config.db_url)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

SQLModel.metadata.create_all(engine)
