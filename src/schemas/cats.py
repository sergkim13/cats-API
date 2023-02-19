from enum import Enum

from fastapi import Query
from pydantic import BaseModel, Field


class CatColor(str, Enum):
    black = "black"
    white = "white"
    black_and_white = "black & white"
    red = "red"
    red_and_white = "red & white"
    red_and_black_and_white = "red & black & white"


class CatBase(BaseModel):
    color: CatColor
    tail_length: int = Field(ge=1)
    whiskers_length: int = Field(ge=1)


class CatInfo(CatBase):
    name: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Masyanya",
                "color": "black & white",
                "tail_length": 12,
                "whiskers_length": 7,
            },
        }


class CatCreate(CatInfo):
    pass


class CatUpdate(BaseModel):
    color: CatColor | None
    tail_length: int | None = Field(ge=1)
    whiskers_length: int | None = Field(ge=1)

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "color": "black",
                "tail_length": 4,
                "whiskers_length": 1,
            },
        }


class CatsQuery(BaseModel):
    attribute: str = Query(default="name")
    order: str = Query(default="asc")
    offset: int = Query(default=0, ge=0)
    limit: int | None = Query(default=None, ge=1)


class Message(BaseModel):
    status: bool
    message: str

    class Config:
        orm_mode = True
