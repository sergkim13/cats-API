from uuid import uuid4

from pydantic import UUID4, BaseModel, Field, validator


class CatsByColors(BaseModel):
    name: str
    color: str
    tail_length: int
    whiskers_length: int