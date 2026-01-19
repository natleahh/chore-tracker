"""Defines database endpoints for directly querying from the shopping list table."""

from typing import Annotated
from fastapi import APIRouter, Depends, Form

from app import services
from app.db import SessionDep, tables


def get_service(session: SessionDep):
    return services.Chore(session=session)


ServiceDep = Annotated[services.Chore, Depends(get_service)]

router = APIRouter()


@router.get("/")
def read_list(service: ServiceDep):
    return service.read_all()


@router.get("/{id}")
def read(service: ServiceDep, id: int):
    return service.read_by_pk(primary_key=id)


@router.post("/")
def create_list(service: ServiceDep, new_chore: Annotated[tables.Chore, Form()]):
    return service.create(new_chore, new_chore)
