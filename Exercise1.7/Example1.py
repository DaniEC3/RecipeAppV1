from sqlalchemy import create_engine
# generates the declarative base class
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

engine = create_engine("mysql://cf-python:password@localhost/my_database")
Base = declarative_base()

class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))