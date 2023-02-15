from http import HTTPStatus
from fastapi import APIRouter
from src.services.helper import get_helper_service, HelperService
from fastapi import Depends


router = APIRouter(
    prefix='/cats',
    tags=['Cats'],
)

@router.get(
    path='',
    status_code=HTTPStatus.OK,
)
async def  