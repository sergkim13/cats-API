from http import HTTPStatus
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.crud.cats_crud import CatsCRUD
from src.database.database_settings import get_session


class CatsService:
    def __init__(self, cats_crud: CatsCRUD) -> None:
        self.cats_crud = cats_crud

    async def get_cats_list(self, attribute, limit, offset):
        try:
            return await self.cats_crud.get_cats_list(attribute, limit, offset)
        except AttributeError:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="Wrong query parameters",
            )


def get_cats_service(session: AsyncSession = Depends(get_session)):
    cats_crud = CatsCRUD(session=session)
    return CatsService(cats_crud=cats_crud)
