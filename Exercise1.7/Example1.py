from sqlalchemy import create_engine
# generates the declarative base class // additional properties from SQLAlchemy’s ORM system
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

engine = create_engine(
    "mysql://cf-python:password@localhost/my_database",
    # echo=True  # optional: logs SQL so you can see what's happening
)
Base = declarative_base()
Base.metadata.create_all(engine)

class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

