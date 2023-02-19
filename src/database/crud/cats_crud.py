from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import asc, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Cats


class CatsCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_cats_list(
        self,
        attribute: str,
        order: str,
        offset: int,
        limit: int | None = None,
    ):
        cats_count = await self._count_cats()
        if cats_count > 0 and offset >= cats_count:
            offset = cats_count - 1
        try:
            if order == "desc":
                sort_order = desc(getattr(Cats, attribute))
            else:
                sort_order = asc(getattr(Cats, attribute))
        except AttributeError:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"Table Cats has no attribute: {attribute}",
            )

        query = select(Cats).order_by(sort_order).offset(offset).limit(limit)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def _count_cats(self):
        query = select(func.count(Cats.name))
        result = await self.session.execute(query)
        count = result.scalar_one()
        return count
