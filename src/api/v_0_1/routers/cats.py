from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.schemas.cats import CatsQuery
from src.services.cats import CatsService, get_cats_service

router = APIRouter(
    prefix="/cats",
    tags=["Cats"],
)


@router.get(
    path="",
    status_code=HTTPStatus.OK,
)
async def get_cats(cats_service: CatsService = Depends(get_cats_service), query: CatsQuery = Depends()):
    return await cats_service.get_cats_list(query)
