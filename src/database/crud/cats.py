from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import asc, desc, func, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Cats
from src.schemas.cats import CatCreate, CatUpdate


class CatsCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def read_all(
        self,
        attribute: str,
        order: str,
        offset: int,
        limit: int | None = None,
    ):
        cats_count = await self._count_all()
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

    async def read(self, name: str):
        query = select(Cats).where(Cats.name == name)
        result = await self.session.execute(query)
        cat = result.scalars().first()
        if not cat:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail=f"Cat with name {name} not found",
            )
        return cat

    async def create(self, data: CatCreate):
        new_cat = Cats(**data.dict())
        try:
            self.session.add(new_cat)
            await self.session.commit()
            await self.session.refresh(new_cat)
            return new_cat
        except IntegrityError:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=f"Cat with name {new_cat.name} already exists",
            )

    async def update(self, name: str, patch: CatUpdate):
        cat_to_update = await self.read(name)
        values = patch.dict(exclude_unset=True)
        for key, value in values.items():
            if not value:
                values[key] = cat_to_update[key]
        stmt = update(Cats).where(Cats.name == name).values(**values)
        await self.session.execute(stmt)
        await self.session.commit()
        await self.session.refresh(cat_to_update)
        return cat_to_update

    async def delete(self, name: str):
        cat_to_delete = await self.read(name)
        await self.session.delete(cat_to_delete)
        await self.session.commit()

    async def _count_all(self):
        query = select(func.count(Cats.name))
        result = await self.session.execute(query)
        count = result.scalar_one()
        return count
