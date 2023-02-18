from http import HTTPStatus

import pytest


@pytest.mark.asyncio
async def test_get_cats_empty(client):
    response = await client.get("/cats")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == []
