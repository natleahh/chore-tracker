"""Defines database endpoints for directly querying from the shopping list table."""

from typing import Annotated
from fastapi import APIRouter, Depends

from app import services
from app.db import SessionDep, tables


def _get_service(session: SessionDep):
    return services.Completion(session=session)


ServiceDep = Annotated[services.Completion, Depends(_get_service)]

router = APIRouter()


@router.get('/')
def read_completion(service: ServiceDep):
    """Reads all completions from the database."""
    return service.read_all()


@router.get('/{id}')
def read(service: ServiceDep, id: int):
    """Reads a completion log from the database by ID."""
    return service.read_by_pk(primary_key=id)


@router.post('/')
def create_completion(service: ServiceDep, new_chore_completion: tables.Completion):
    """Adds a new completion log to the database."""
    return service.create(new_chore_completion)


@router.post('/now/{chore_id}')
def complete_now(service: ServiceDep, chore_id: int):
    """Completes a chore now."""
    chore_service = services.Chore(session=service._db)
    chore: tables.Chore = chore_service.read_by_pk(primary_key=chore_id, raise_error=True)
    return service.complete_chore_now(chore=chore)
