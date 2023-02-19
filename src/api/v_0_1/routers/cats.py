from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.schemas.cats import CatCreate, CatInfo, CatsQuery, CatUpdate, Message
from src.services.cats import CatsService, get_cats_service

router = APIRouter(
    prefix="/cats",
    tags=["Cats"],
)


@router.get(path="", status_code=HTTPStatus.OK, response_model=list[CatInfo], summary="Получить список всех котов")
async def get_cats(
    cats_service: CatsService = Depends(get_cats_service),
    query: CatsQuery = Depends(),
) -> list[CatInfo]:
    return await cats_service.get_cats_list(query)


@router.get(path="/{name}", status_code=HTTPStatus.OK, response_model=CatInfo, summary="Получить информацию о коте")
async def get_cat(
    name: str,
    cats_service: CatsService = Depends(get_cats_service),
) -> CatInfo:
    return await cats_service.get_cat(name)


@router.post(path="", status_code=HTTPStatus.CREATED, response_model=CatInfo, summary="Добавить нового кота")
async def post_cat(
    new_cat: CatCreate,
    cats_service: CatsService = Depends(get_cats_service),
) -> CatInfo:
    return await cats_service.create_cat(new_cat)


@router.patch(
    path="/{name}",
    status_code=HTTPStatus.OK,
    response_model=CatInfo,
    summary="Обновить информаицю о коте",
)
async def patch_cat(
    name: str,
    patch: CatUpdate,
    cats_service: CatsService = Depends(get_cats_service),
) -> CatInfo:
    return await cats_service.update_cat(name, patch)


@router.delete(
    path="/{name}",
    status_code=HTTPStatus.OK,
    response_model=Message,
    summary="Удалить кота",
)
async def delete_cat(
    name: str,
    cats_service: CatsService = Depends(get_cats_service),
) -> Message:
    return await cats_service.delete_cat(name)
