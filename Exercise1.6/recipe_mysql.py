import pickle
import mysql.connector

main_data = {}
recipes_list = []
ingredients_list = []
conn = mysql.connector.connect(
host='localhost',
user='cf-python',
passwd='password')
cursor = conn.cursor()

def initialize_app():
    print("\nWelcome to the Recipe App!\n")
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
    cursor.execute("USE task_database")
    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes(
        id             INT AUTO_INCREMENT PRIMARY KEY,
        name           VARCHAR(100),
        ingredients    TEXT,
        cook_time      INT,
        difficulty     VARCHAR(20)
    )''')
    cursor.execute("SELECT name, ingredients, cook_time, difficulty FROM recipes")
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        recipe = {
            "name": row[0],
            "Ingredients": [ingredient.strip() for ingredient in row[1].split(',')],
            "Cooking Time (Minutes)": row[2],
            "Difficulty": row[3]
        }
        recipes_list.append(recipe)
        for ingredient in recipe["Ingredients"]:
            if ingredient not in ingredients_list:
                ingredients_list.append(ingredient)
  
def showing_recipes():
    print("\nFinal Recipes List with Difficulty Levels:")
    for recipe in recipes_list:
        print("------------------------\n")
        print("Recipe Name:", recipe["name"], "\n")
        print("Cooking Time (Minutes):", recipe["Cooking Time (Minutes)"])
        print("Ingredients:")
        for ingredient in recipe["Ingredients"]:
            print("-", ingredient)
        print("Difficulty Level:", recipe.get("Difficulty", "Not Assigned"))
        print("------------------------\n")

def showing_ingredients():
    print("\nUnique Ingredients List:")
    print("------------------------")
    sorted_ingredients = sorted(ingredients_list)
    for ingredient in sorted_ingredients:
        print("-", ingredient)  
    print("------------------------\n")

def create_recipe():
    print("\n----- Adding a New Recipe -----\n")
    recipe_name = str(input("Enter the recipe name: "))
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')

    recipe = {
        "name": recipe_name,
        "Cooking Time (Minutes)": int(cooking_time),
        "Ingredients": [ingredient.strip() for ingredient in ingredients]
    }

    recipes_list.append(recipe)
    for ingredient in recipe["Ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.extend([ingredient])
    main_data["recipes_list"] = recipes_list
    main_data["all_ingredients"] = ingredients_list
    calc_difficult()
    print(f"Recipe '{recipe_name}' added successfully!\n")  
    add_recipe()

def add_recipe():
  for recipe in recipes_list:
      cursor.execute("INSERT INTO recipes (name, ingredients, cook_time, difficulty) VALUES (%s, %s, %s, %s)",
                      (recipe["name"], ",".join(recipe["Ingredients"]), recipe["Cooking Time (Minutes)"], recipe.get("Difficulty", "Not Assigned")))
  conn.commit()

  print("Exiting the Recipe App. Goodbye!")

def calc_difficult():
    for recipe in recipes_list:
        if recipe["Cooking Time (Minutes)"] < 10 and len(recipe["Ingredients"]) < 4:          
            recipe["Difficulty"] = "Easy"
        elif recipe["Cooking Time (Minutes)"] < 10 and len(recipe["Ingredients"]) >= 4:         
            recipe["Difficulty"] = "Medium"
        elif recipe["Cooking Time (Minutes)"] >= 10 and len(recipe["Ingredients"]) < 4:         
            recipe["Difficulty"] = "Intermediate"
        else:  
            recipe["Difficulty"] = "Hard"
       
def search_recipes_by_name(recipes_list, all_ingredients):
    recipe_name = input("Enter the recipe name to search: ").strip().lower()
    found = False
    for recipe in recipes_list:
        if recipe["name"].lower() == recipe_name:
            print("\nRecipe Found:")
            print("------------------------\n")
            print("Recipe Name:", recipe["name"], "\n")
            print("Cooking Time (Minutes):", recipe["Cooking Time (Minutes)"])
            print("Ingredients:")
            for ingredient in recipe["Ingredients"]:
                print("-", ingredient)
            print("Difficulty Level:", recipe.get("Difficulty", "Not Assigned"))
            print("------------------------\n")
            found = True
            break
    if not found:
        print(f"Recipe '{recipe_name}' not found.")

def search_recipes_by_ingredient(all_ingredients, recipes_list):
    index_ingredients = print_sorted_ingredients_list(all_ingredients)
    try:
        number = int(input("Enter the number of the ingredient to search (or press Enter to skip): ").strip())
        if number in index_ingredients:
            ingredient_name = index_ingredients[number]
            print(f"Ingredient '{ingredient_name}' is available.")
        else:
            print("Number out of range.")
            KeyError # Trigger KeyError for out of range / Can be change for a while loop instead
            
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyError:
        print("Ingredient not found in the index.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        recipes_matching = []
        title = False
        for recipe in recipes_list:
            if ingredient_name in recipe["Ingredients"]:
                if not title:
                    print(f"\nRecipes containing '{ingredient_name}':")
                    title = True
                print("------------------------\n")
                print("Recipe Name:", recipe["name"], "\n")
                print("Cooking Time (Minutes):", recipe["Cooking Time (Minutes)"])
                print("Ingredients:")
                for ingredient in recipe["Ingredients"]:
                    print("-", ingredient)
                print("Difficulty Level:", recipe.get("Difficulty", "Not Assigned"))
                print("------------------------\n")
                recipes_matching.append(recipe["name"])
        if not recipes_matching:
            print(f"No recipes found containing the ingredient '{ingredient_name}'.")

def print_sorted_ingredients_list(all_ingredients):
    print("\nAvailable Ingredients List:")
    print("------------------------")
    sorted_ingredients = sorted(all_ingredients)
    index_ingredients = {}
    for i, ingredient in enumerate(sorted_ingredients, start=1):
        print(f"{i}. {ingredient}")
        index_ingredients[i] = ingredient
    print("------------------------\n")
    return index_ingredients

def main_menu():
    print("//================Recipe App Menu ================\\\\\n")
    opt = int(input('''Choose an option (1-8):\n
    1. Show all recipes\n    
    2. Show ingredients\n                           
    3. Add a recipe\n
    4. Search recipe by name\n
    5. Search recipe by ingredient\n
    6. Update a recipe\n
    7. Delete a recipe\n 
    8. Exit\n''' ))

    while opt > 8 or opt < 1:
        opt = int(input("\nInvalid option. Please choose a number between 1 and 8.\n"))
    if opt == 1:
        showing_recipes()
        main_menu()
    elif opt == 2:
        showing_ingredients()
        main_menu()
    elif opt == 3:
        create_recipe()
        main_menu()
    elif opt == 4:
        search_recipes_by_name(recipes_list, ingredients_list)
        main_menu()
    elif opt == 5:
        search_recipes_by_ingredient(ingredients_list, recipes_list)
        main_menu()
    elif opt == 6:  
        print("Update a recipe - Feature coming soon!")
        main_menu()
    elif opt == 7:  
        print("Delete a recipe - Feature coming soon!")
        main_menu()
    else:
        print("Exiting the Recipe App. Goodbye!") 
        exit()


def main():
  initialize_app()
  main_menu()
main()