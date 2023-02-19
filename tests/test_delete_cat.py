from http import HTTPStatus

import pytest

from tests.conftest import CAT_1


@pytest.mark.asyncio
@pytest.mark.usefixtures("fake_cat")
async def test_delete_cat(client):
    response = await client.delete(f"/cats/{CAT_1['name']}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"status": True, "message": f"Cat {CAT_1['name']} has been deleted"}


@pytest.mark.asyncio
async def test_delete_cat_not_existing(client):
    response = await client.delete(f"/cats/{CAT_1['name']}")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": f"Cat with name {CAT_1['name']} not found"}
