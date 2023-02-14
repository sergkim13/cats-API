from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select, insert
from src.database.models import Cats, CatColorsInfo, CatsStat
from sqlalchemy.exc import IntegrityError


class HelperCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_colors_list(self):
        query = select(Cats.color).group_by(Cats.color)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_tail_length_list(self):
        query = select(Cats.tail_length)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_whiskers_length_list(self):
        query = select(Cats.whiskers_length)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def count_color(self, color: str):
        query = select(func.count(Cats.color)).where(Cats.color == color)
        result = await self.session.execute(query)
        return result.scalar_one()


    async def insert_color_count(self, color: str, count: int):
        stmt = insert(CatColorsInfo).values(color=color, count=count)
        try:
            await self.session.execute(stmt)
            await self.session.commit()
            return 'OK'
        except IntegrityError:
            return f"Key '{color}' already exists."

    async def insert_colors_stat(self, values: list):
        stmt = insert(CatsStat).values(values)
        await self.session.execute(stmt)
        await self.session.commit()
        return 'OK'