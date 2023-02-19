from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.crud.cats import CatsCRUD
from src.database.database_settings import get_session
from src.schemas.cats import Cat, CatsQuery


class CatsService:
    def __init__(self, cats_crud: CatsCRUD) -> None:
        self.cats_crud = cats_crud

    async def get_cats_list(
        self,
        query: CatsQuery,
    ) -> list[Cat]:
        if query.order not in ["asc", "desc"]:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"Wrong query parameter: {query.order}",
            )
        return await self.cats_crud.read_all(query.attribute, query.order, query.offset, query.limit)

    async def create_cat(self, data: Cat) -> Cat:
        return await self.cats_crud.create(data)


def get_cats_service(session: AsyncSession = Depends(get_session)):
    cats_crud = CatsCRUD(session=session)
    return CatsService(cats_crud=cats_crud)
