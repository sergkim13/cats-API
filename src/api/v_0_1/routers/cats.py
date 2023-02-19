from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.schemas.cats import Cat, CatsQuery
from src.services.cats import CatsService, get_cats_service

router = APIRouter(
    prefix="/cats",
    tags=["Cats"],
)


@router.get(
    path="",
    status_code=HTTPStatus.OK,
    response_model=list[Cat],
)
async def get_cats(
    cats_service: CatsService = Depends(get_cats_service),
    query: CatsQuery = Depends(),
) -> list[Cat]:
    return await cats_service.get_cats_list(query)


@router.post(
    path="",
    status_code=HTTPStatus.CREATED,
    response_model=Cat,
)
async def post_cats(
    new_cat: Cat,
    cats_service: CatsService = Depends(get_cats_service),
) -> Cat:
    return await cats_service.create_cat(new_cat)
