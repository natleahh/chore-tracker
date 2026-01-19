"""Main app entry point."""

from fastapi import FastAPI

from app.api.v1 import chores

app = FastAPI()

# register routes
app.include_router(chores.router, prefix="/v1/chore")
