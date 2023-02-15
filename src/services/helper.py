import statistics

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.crud import HelperCRUD
from src.database.database_settings import get_session


class HelperService:
    def __init__(self, helper_crud: HelperCRUD) -> None:
        self.helper_crud = helper_crud

    async def fill_cat_colors_info(self):
        colors_dict = await self.count_cats_by_color()
        for color, count in colors_dict.items():
            result = await self.helper_crud.insert_color_count(color, count)
            if result != "OK":
                return result
        return "OK"

    async def fill_cats_stat(self):
        tail_length_list = await self.helper_crud.get_tail_length_list()
        whiskers_length_list = await self.helper_crud.get_whiskers_length_list()
        print("Хвосты", tail_length_list)
        print("УСЫ", whiskers_length_list)
        lengths_list = []
        lengths_list.append(self.count_mean(tail_length_list))
        lengths_list.append(self.count_median(tail_length_list))
        lengths_list.append(self.count_mode(tail_length_list))
        lengths_list.append(self.count_mean(whiskers_length_list))
        lengths_list.append(self.count_median(whiskers_length_list))
        lengths_list.append(self.count_mode(whiskers_length_list))
        result = await self.helper_crud.insert_colors_stat(lengths_list)
        return result

    async def count_cats_by_color(self):
        colors_dict = {}
        cat_colors = await self.helper_crud.get_colors_list()
        for color in cat_colors:
            count = await self.helper_crud.count_color(color)
            colors_dict[color] = count
        return colors_dict

    @staticmethod
    def count_mean(value_list: list):
        return round(statistics.mean(value_list), 2)

    @staticmethod
    def count_median(value_list: list):
        return statistics.median(value_list)

    @staticmethod
    def count_mode(value_list: list):
        return statistics.multimode(value_list)


def get_helper_service(session: AsyncSession = Depends(get_session)):
    helper_crud = HelperCRUD(session=session)
    return HelperService(helper_crud=helper_crud)
