from sqlalchemy import create_engine
# generates the declarative base class // additional properties from SQLAlchemy’s ORM system
from sqlalchemy import orm
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

#  Create an engine that connects to the MySQL database
engine = create_engine(
    "mysql+mysqlconnector://cf-python:password@localhost/my_database",
    # echo=True  # optional: logs SQL so you can see what's happening
)
Base = orm.declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        # When printing recipe *print(recipe)*
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
# Create the table in the database
Base.metadata.create_all(engine)
tea = Recipe(
    name = "Tea",
    cooking_time = 5,
    ingredients = "Tea Leaves, Water, Sugar "
)
session.add(tea)
session.commit()

recipes_list = session.query(Recipe).all()

for recipe in recipes_list:
    print("\nRecipe ID: ", recipe.id)
    print("Recipe Name: ", recipe.name)
    print("Ingredients: ", recipe.ingredients)
    print("Cooking Time: ", recipe.cooking_time, "\n")

# session.query(Recipe).filter(Recipe.name == 'Coffee').all()
session.query(Recipe).filter(Recipe.name == 'Coffee').one()
recipes_list[0].ingredients

# Appending our new ingredient -
recipes_list[0].ingredients += ', Cardamom'

# Checking to see if it's alright -
recipes_list[0].ingredients
'Tea Leaves, Water, Sugar, Cardamom'

# And finally, we commit our changes -
session.commit()