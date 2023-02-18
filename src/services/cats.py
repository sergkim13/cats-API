from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.crud.cats_crud import CatsCRUD
from src.database.database_settings import get_session
from src.schemas.cats import CatsQuery


class CatsService:
    def __init__(self, cats_crud: CatsCRUD) -> None:
        self.cats_crud = cats_crud

    async def get_cats_list(
        self,
        query: CatsQuery,
    ):
        if query.order not in ["asc", "desc"]:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"Wrong query parameter: {query.order}",
            )
        return await self.cats_crud.get_cats_list(query.attribute, query.order, query.offset, query.limit)


def get_cats_service(session: AsyncSession = Depends(get_session)):
    cats_crud = CatsCRUD(session=session)
    return CatsService(cats_crud=cats_crud)
