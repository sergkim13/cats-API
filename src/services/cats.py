from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.crud.cats import CatsCRUD
from src.database.database_settings import get_session
from src.schemas.cats import CatCreate, CatInfo, CatsQuery, CatUpdate, Message


class CatsService:
    def __init__(self, cats_crud: CatsCRUD) -> None:
        self.cats_crud = cats_crud

    async def get_cats_list(
        self,
        query: CatsQuery,
    ) -> list[CatInfo]:
        if query.order not in ["asc", "desc"]:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"Wrong query parameter: {query.order}",
            )
        return await self.cats_crud.read_all(query.attribute, query.order, query.offset, query.limit)

    async def get_cat(self, name: str) -> CatInfo:
        return await self.cats_crud.read(name)

    async def create_cat(self, data: CatCreate) -> CatInfo:
        return await self.cats_crud.create(data)

    async def update_cat(self, name: str, patch: CatUpdate) -> CatInfo:
        return await self.cats_crud.update(name, patch)

    async def delete_cat(self, name: str) -> Message:
        await self.cats_crud.delete(name)
        return Message(status=True, message=f"Cat {name} has been deleted")


def get_cats_service(session: AsyncSession = Depends(get_session)):
    cats_crud = CatsCRUD(session=session)
    return CatsService(cats_crud=cats_crud)
