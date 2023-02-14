import asyncio
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, distinct, func, select, update
from database.database_settings import get_db
from database.models import Cats


async def count_cats_by_color():
    query = select(Cats.color, func.count(Cats.color)).group_by(Cats.color)
    result = await session.execute(query)
    return result.all


async def main():
    await count_cats_by_color()

if __name__ == '__main__':
    asyncio.run(main())
