from sqlalchemy import ARRAY, Column, Enum, Integer, Numeric, String

from src.database.database_settings import Base

CAT_COLOR_LIST = [
    "black",
    "white",
    "black & white",
    "red",
    "red & white",
    "red & black & white",
]


class Cats(Base):
    __tablename__ = "cats"

    name = Column(String, primary_key=True, nullable=False)
    color = Column(Enum(*CAT_COLOR_LIST, name="cat_color"))
    tail_length = Column(Integer)
    whiskers_length = Column(Integer)


class CatColorsInfo(Base):
    __tablename__ = "cat_colors_info"

    color = Column(Enum(*CAT_COLOR_LIST, name="cat_color"), primary_key=True, unique=True)
    count = Column(Integer)


class CatsStat(Base):
    __tablename__ = "cats_stat"

    tail_length_mean = Column(Numeric(4, 2), primary_key=True)
    tail_length_median = Column(Numeric)
    tail_length_mode = Column(ARRAY(Integer))
    whiskers_length_mean = Column(Numeric(4, 2))
    whiskers_length_median = Column(Numeric)
    whiskers_length_mode = Column(ARRAY(Integer))
