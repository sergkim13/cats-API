from http import HTTPStatus

import pytest


@pytest.mark.asyncio
@pytest.mark.usefixtures("fake_cats")
async def test_get_cats(client):
    response = await client.get("/cats")
    assert response.status_code == HTTPStatus.OK
    print(response.json())
    assert response.json() == [
        {"name": "Barsik", "color": "black", "tail_length": 12, "whiskers_length": 7},
        {"name": "Vasya", "color": "red", "tail_length": 8, "whiskers_length": 3},
    ]


@pytest.mark.asyncio
@pytest.mark.usefixtures("fake_cats")
async def test_get_cats_with_query(client):
    response = await client.get("/cats?attribute=color&order=desc&offset=1&limit=1")
    assert response.status_code == HTTPStatus.OK
    print(response.json())
    assert response.json() == [{"name": "Barsik", "color": "black", "tail_length": 12, "whiskers_length": 7}]


@pytest.mark.asyncio
@pytest.mark.usefixtures("fake_cats")
async def test_get_cats_offset_out_of_range(client):
    response = await client.get("/cats?offset=999&limit=1")
    assert response.status_code == HTTPStatus.OK
    print(response.json())
    assert response.json() == [{"name": "Vasya", "color": "red", "tail_length": 8, "whiskers_length": 3}]


@pytest.mark.asyncio
async def test_get_cats_empty(client):
    response = await client.get("/cats")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == []


@pytest.mark.asyncio
async def test_get_cats_wrong_order(client):
    response = await client.get("/cats?order=not_exist_order")
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Wrong query parameter: not_exist_order"}


@pytest.mark.asyncio
async def test_get_cats_wrong_attribute(client):
    response = await client.get("/cats?attribute=not_exist_attr")
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": "Table Cats has no attribute: not_exist_attr"}
