from sqlalchemy import func, insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Cats


class CatsCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_cats_list(
            self,
            attribute: str | None,
            limit: int | None = None,
            offset: int | None = None,
    ):
        if not attribute:
            attribute = "name"
        query = select(Cats).order_by(getattr(Cats, attribute)).offset(offset).limit(limit)
        result = await self.session.execute(query)
        return result.scalars().all()
