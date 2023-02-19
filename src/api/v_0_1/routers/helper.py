from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.services.helper import HelperService, get_helper_service

router = APIRouter(
    prefix="/helper",
    tags=["Helpers"],
)


@router.post(
    path="/fill_in_cat_colors_info",
    status_code=HTTPStatus.CREATED,
    summary="Посчитать кол-во котов в разбивке по цветам и занести информацию в таблицу Cat_colors_info",
)
async def fill_in_cat_colors_info(helper_service: HelperService = Depends(get_helper_service)):
    return await helper_service.fill_cat_colors_info()


@router.post(
    path="/fill_in_cats_stat",
    status_code=HTTPStatus.CREATED,
    summary="Посчитать статистику по усам и хвостам котов и занести информацию в таблицу Cats_stat",
)
async def fill_in_cats_stat(helper_service: HelperService = Depends(get_helper_service)):
    return await helper_service.fill_cats_stat()
