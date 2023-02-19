from http import HTTPStatus

import pytest

from tests.conftest import CAT_1


@pytest.mark.asyncio
async def test_post_cat(client):
    response = await client.post("/cats", json=CAT_1)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == CAT_1


@pytest.mark.asyncio
@pytest.mark.usefixtures("fake_cat")
async def test_post_cat_already_exist(client):
    response = await client.post("/cats", json=CAT_1)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {"detail": f"Cat with name {CAT_1['name']} already exists"}
