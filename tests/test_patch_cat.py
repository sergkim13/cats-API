from http import HTTPStatus

import pytest

from tests.conftest import CAT_1, CAT_1_PATCH, CAT_1_UPDATED


@pytest.mark.asyncio
@pytest.mark.usefixtures("fake_cat")
async def test_patch_cat(client):
    response = await client.patch(f"/cats/{CAT_1['name']}", json=CAT_1_PATCH)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == CAT_1_UPDATED


@pytest.mark.asyncio
async def test_patch_cat_not_existing(client):
    response = await client.patch(f"/cats/{CAT_1['name']}", json=CAT_1_PATCH)
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": f"Cat with name {CAT_1['name']} not found"}
