from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.services.cats import CatsService, get_cats_service

router = APIRouter(
    prefix="/cats",
    tags=["Cats"],
)


@router.get(
    path="",
    status_code=HTTPStatus.OK,
)
async def get_cats(
    cats_service: CatsService = Depends(get_cats_service),
    attribute: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
):
    return await cats_service.get_cats_list(attribute, limit, offset)
