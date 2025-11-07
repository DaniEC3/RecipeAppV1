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
    __tablename__ = "final_project_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def calculate_difficulty(self):
        ingredients_list = [i.strip() for i in self.ingredients.split(",") if i.strip()]

        num_ingredients = len(ingredients_list)

        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        return [i.strip() for i in self.ingredients.split(",") if i.strip()]
    
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + "Difficulty:"+ self.difficulty + ">"
    
    def __str__(self):
        return (
            "\n" + "="*40 + "\n"
            f"\n🍲  Recipe Name:\t{self.name}\n"
            f"⏱️  Cooking Time:\t{self.cooking_time} minutes\n"
            f"🧂  Ingredients:\t{self.ingredients}\n"
            f"💪  Difficulty:\t{self.difficulty}\n\n"
            + "="*40
    )

# Create the table in the database
Base.metadata.create_all(engine)

def initialize_app():
    # not necessary to add tea every time the app runs
    recipes_list = session.query(Recipe).all()  

    if session.query(Recipe).filter(Recipe.name == 'Tea').first() not in recipes_list:
        tea = Recipe(
            
        name = "Tea",
        cooking_time = 5,
        ingredients = "Tea Leaves, Water, Sugar "
    )
        tea.calculate_difficulty()
        session.add(tea)
        session.commit()

def showing_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("\nNo recipes found in the database.\n")
    else:
        print("\n//================ All Recipes ================\\\\\n")
    for i, recipe in enumerate(recipes, start=1):
        print("\n------------------------------\n")
        print("Recipe ID: ", i)
        print(recipe)  # <-- automatically calls __str__()
    
def create_recipe():
    print("\n//================ Add a New Recipe ================\\\\\n")
    name = input("Enter the recipe name: ")

    name_flag = False

    while not name_flag:
        if len(name.strip()) == 0:
            name = input("Recipe name cannot be empty. Please enter the recipe name: ")
        elif len(name) > 50:
            name = input("Recipe name is too long (max 50 characters). Please enter a shorter name: ")
        elif name.isdigit():
            name = input("Recipe name cannot be just numbers. Please enter a valid name: ")
        elif not name.isalpha() and " " not in name:
            name = input("Recipe name must contain alphabetic characters. Please enter a valid name: ")
        else:
            name_flag = True

    cooking_time_flag = False

    while not cooking_time_flag:
        try:
            cooking_time = int(input("Enter the cooking time (in minutes): "))
            if cooking_time < 1:
                print("⚠️ Cooking time must be at least 1 minute.")
            elif cooking_time > 1440:
                print("⚠️ Cooking time is too long (max 1440 minutes).")
            else:
                cooking_time_flag = True
        except ValueError:
            print("⚠️ Please enter a valid number for cooking time.")
        
    number_of_ingredients = int(input("Enter the number of ingredients: "))
    while number_of_ingredients < 1:
        print("⚠️ There must be at least one ingredient.")
        number_of_ingredients = int(input("Enter the number of ingredients: "))
    
    ingredients = ""
    
    for i in range(number_of_ingredients):
        ingredient = input(f"Enter ingredient {i+1}: ")
        while True: 
            try:
                if len(ingredient.strip()) == 0:
                    raise ValueError("Ingredient name cannot be empty.")
                elif len(ingredient) > 50:
                    raise ValueError("Ingredient name is too long (max 50 characters).")
                elif ingredient.isdigit():
                    raise ValueError("Ingredient name cannot be just numbers.")
            except ValueError as ve:
                print("⚠️ Invalid input. Please enter a valid ingredient.")
            else:
                break
        if i == 0:
            ingredients = ingredient
        else:
            ingredients += f", {ingredient}"
 
    new_recipe = Recipe(
        name=name,
        cooking_time=cooking_time,
        ingredients=ingredients
    )
    new_recipe.calculate_difficulty()
    print("\nAdding the following recipe to the database:")
    print(new_recipe)
    session.add(new_recipe)
    session.commit()
    print(f"\n✅ Recipe '{name}' added successfully!\n")

def search_recipes_by_ingredient():
    print("\n//================ Search Recipes by Ingredient ================\\\\\n")
    list_of_ings = []
    for recipe in session.query(Recipe).all():
        list_of_ings.extend(recipe.return_ingredients_as_list())
    print("Available ingredients in the database:\n")
    for i, ing in enumerate(set(list_of_ings), start=1):
        print(f"{i}. {ing}")
    print("\n")

    while True:
        try:
            op_ingredient_search = int(input("Enter the number of the ingredient to search for: ").strip())
            if op_ingredient_search < 1 or op_ingredient_search > len(set(list_of_ings)):
                raise ValueError("Invalid ingredient selection.")
            elif op_ingredient_search is None:
                raise ValueError("Input cannot be empty.")
            elif not op_ingredient_search.is_integer():
                raise ValueError("Input must be a number.")
        except ValueError:
            print("⚠️ Please enter a valid number corresponding to an ingredient\n ")
        else:
            break

    recipe_check = session.query(Recipe).count()
    found_recipes = []

    if recipe_check == 0:
        print("⚠️ No recipes found in the database.")
        return
    ingredient_search = list(set(list_of_ings))[op_ingredient_search - 1]
    for recipe in session.query(Recipe).all():
        if ingredient_search.lower() in [ing.lower() for ing in recipe.return_ingredients_as_list()]:
            found_recipes.append(recipe)

    if not found_recipes:
        print(f"\nNo recipes found containing the ingredient '{ingredient_search}'.\n")
    else:
        print(f"\nRecipes containing the ingredient '{ingredient_search}':\n")
        for i, recipe in enumerate(found_recipes, start=1):
            print("\n------------------------------\n")
            print("Recipe ID: ", i)
            print(recipe)  # <-- automatically calls __str__()

def update_recipe():
    recipes_in_db = session.query(Recipe).all()
    if not recipes_in_db:
        print("\nNo recipes found in the database to update.\n")
        return
    print("\n//================ Update a Recipe ================\\\\\n")
    for i, recipe in enumerate(recipes_in_db, start=1):
        print("\n------------------------------\n")
        print("Recipe ID: ", i)
        print(recipe)  # <-- automatically calls __str__()
    while True:
        try:
            recipe_id_to_update = int(input("Enter the Recipe ID of the recipe you want to update: ").strip()) - 1
            if recipe_id_to_update < 0 or recipe_id_to_update >= len(recipes_in_db):
                raise IndexError("Invalid Recipe ID.")
            elif recipe_id_to_update is None:
                raise ValueError("Input cannot be empty.")
            elif not recipe_id_to_update.is_integer():
                raise ValueError("Input must be a number.")
        except IndexError:
            print("⚠️ Recipe ID out of range. Please try again.\n")
        except ValueError:
            print("⚠️ Please enter a valid Recipe ID number.\n")
        else:
            break
    recipe_to_update = recipes_in_db[recipe_id_to_update]
    print(f"\nYou have selected to update the recipe:\n{recipe_to_update}\n")
    # Updating fields
    # Name
    while True:
        new_name = input("Enter the new recipe name (leave blank to keep current): ").strip()
        if not new_name:
            print("Keeping current recipe name.")
            break
        elif len(new_name) > 50:
            print("⚠️ Recipe name is too long (max 50 characters). Please enter a shorter name.")
        elif new_name.isdigit():
            print("⚠️ Recipe name cannot be just numbers. Please enter a valid name.")
        elif not new_name.isalpha() and " " not in new_name:
            print("⚠️ Recipe name must contain alphabetic characters. Please enter a valid name.")
        else:
            recipe_to_update.name = new_name
            session.commit()
            print(f"\n✅ Recipe ID {recipe_to_update.id} updated successfully!\n")
            break
    # Cooking Time 
    while True:
        try:
            new_cooking_time = input("Enter the new cooking time in minutes (leave blank to keep current): ").strip()
            if not new_cooking_time:
                print("Keeping current cooking time.")
                break
            new_cooking_time = int(new_cooking_time)
            if new_cooking_time < 1:
                print("⚠️ Cooking time must be at least 1 minute.")
            elif new_cooking_time > 1440:
                print("⚠️ Cooking time is too long (max 1440 minutes).")
            else:
                recipe_to_update.cooking_time = new_cooking_time
        except ValueError:
            print("⚠️ Please enter a valid number for cooking time.")
            continue
        except ValueError:
            print("⚠️ Please enter a valid number for cooking time.")
        else:
            recipe_to_update.cooking_time = new_cooking_time
            recipe_to_update.calculate_difficulty()
            session.commit()
            print(f"\n✅ Recipe ID {recipe_to_update.id} updated successfully!\n")
            break
    # Ingredients
    while True:
        try:
            number_of_ingredients = input("Enter the new number of ingredients (leave blank to keep current): ").strip()
            if not number_of_ingredients:
                print("Keeping current ingredients.")
                break
            number_of_ingredients = int(number_of_ingredients)
            if number_of_ingredients < 1:
                print("⚠️ There must be at least one ingredient.")
            elif number_of_ingredients >= 50:
                print("⚠️ Too many ingredients (max 50).")
            elif not number_of_ingredients.is_integer():
                print("⚠️ Please enter a valid number for ingredients.")
            elif len(str(number_of_ingredients)) > 255:
                print("⚠️ Please enter a valid number for ingredients.")
        except ValueError:
            print("⚠️ Please enter a valid number for ingredients.")
        else:
            break
    if number_of_ingredients:
        new_ingredients = ""
        for i in range(number_of_ingredients):
            ingredient = input(f"Enter ingredient {i+1}: ")
            while True: 
                try:
                    if len(ingredient.strip()) == 0:
                        raise ValueError("Ingredient name cannot be empty.")
                    elif len(ingredient) > 50:  
                        raise ValueError("Ingredient name is too long (max 50 characters).")
                    elif ingredient.isdigit():
                        raise ValueError("Ingredient name cannot be just numbers.")
                except ValueError as ve:
                    print("⚠️ Invalid input. Please enter a valid ingredient.")
                else:
                    break
            if i == 0:
                new_ingredients = ingredient
            else:
                new_ingredients += f", {ingredient}"
        recipe_to_update.ingredients = new_ingredients
        recipe_to_update.calculate_difficulty()
        session.commit()
        print(f"\n✅ Recipe ID {recipe_to_update.id} updated successfully!\n")

def delete_recipe():
    recipes_in_db = session.query(Recipe).all()
    if not recipes_in_db:
        print("\nNo recipes found in the database to update.\n")
        return
    print("\n//================ Delete a Recipe ================\\\\\n")
    for i, recipe in enumerate(recipes_in_db, start=1):
        print("\n------------------------------\n")
        print("Recipe ID: ", i)
        print(recipe)  # <-- automatically calls __str__()
    while True:
        try:
            recipe_id_to_delete = int(input("\nEnter the Recipe ID of the recipe you want to delete: ").strip()) - 1
            if recipe_id_to_delete < 0 or recipe_id_to_delete >= len(recipes_in_db):
                raise IndexError("Invalid Recipe ID.")
            elif recipe_id_to_delete is None:
                raise ValueError("Input cannot be empty.")
            elif not recipe_id_to_delete.is_integer():
                raise ValueError("Input must be a number.")
            confirmation = input(f"Are you sure you want to delete Recipe ID {recipe_id_to_delete + 1}? (y/n): ").strip().lower()
            if confirmation != 'y':
                print("Deletion cancelled.")
                return
        except IndexError:
            print("⚠️ Recipe ID out of range. Please try again.\n")
        except ValueError:
            print("⚠️ Please enter a valid Recipe ID number.\n")
        else:
            recipe_to_delete = recipes_in_db[recipe_id_to_delete]
            session.delete(recipe_to_delete)
            session.commit()
            print(f"\n✅ Recipe ID {recipe_to_delete.id} deleted successfully!\n")
            break

def main_menu():
    print("\n//================Recipe App Menu ================\\\\\n")
    try:
        opt = int(input('''Choose an option (1-6):\n
        1. Show all recipes\n                              
        2. Add a recipe\n
        3. Update a recipe\n
        4. Search recipes by ingredient\n
        5. Delete a recipe\n
        6. Exit\n''' ))
    except ValueError:
        print("⚠️ Please enter a number between 1 and 6.")
        opt = None
        return opt
    else:

        while opt > 6 or opt < 1:
            opt = int(input("\nInvalid option. Please choose a number between 1 and 6.\n"))
        if opt == 1:
            showing_recipes()
            main_menu()
        elif opt == 2:
            create_recipe()
            main_menu()
        elif opt == 3:  
            update_recipe()
            main_menu()
        elif opt == 4:      
            search_recipes_by_ingredient()
            main_menu()
        elif opt == 5:  
            delete_recipe()
            main_menu()
        else:
            print("Exiting the Recipe App. Goodbye!") 
            session.close()
            exit()
def main():
  print("\nWelcome to the Recipe App!\n")
  initialize_app()
  main_menu()
main()