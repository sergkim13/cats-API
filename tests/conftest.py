import asyncio

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.database.database_settings import get_session
from src.database.models import Base
from src.main import app

# Test database fixtures
SQLALCHEMY_TEST_DATABASE_URL = "postgresql+asyncpg://test:test@localhost:5433/test"


# Test database fixtures
@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(autouse=True, scope="session")
async def create_engine():
    test_engine = create_async_engine(SQLALCHEMY_TEST_DATABASE_URL)

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield test_engine

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def test_session(create_engine):
    connection = await create_engine.connect()
    transaction = await connection.begin()
    test_session = AsyncSession(bind=connection)

    yield test_session

    await transaction.rollback()
    await connection.close()


@pytest_asyncio.fixture(scope="function")
async def client(test_session):
    app.dependency_overrides[get_session] = lambda: test_session

    async with AsyncClient(app=app, base_url="http://test") as test_client:
        yield test_client
