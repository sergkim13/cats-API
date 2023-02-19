from enum import Enum

from fastapi import Query
from pydantic import BaseModel


class CatColor(str, Enum):
    black = "black"
    white = " white"
    black_and_white = " black & white"
    red = "red"
    red_and_white = "red & white"
    red_and_black_and_white = "red & black & white"


class CatsQuery(BaseModel):
    attribute: str = Query(default="name")
    order: str = Query(default="asc")
    offset: int = Query(default=0, ge=0)
    limit: int | None = Query(default=None, ge=1)


class CatCreate(BaseModel):
    name: str
    color: CatColor
    tail_length: int
    whiskers_length: int
