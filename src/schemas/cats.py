from fastapi import Query

from pydantic import BaseModel


class CatsQuery(BaseModel):
    attribute: str = Query(default="name")
    order: str = Query(default="asc")
    offset: int = Query(default=0, ge=0)
    limit: int | None = Query(default=None, ge=1)
