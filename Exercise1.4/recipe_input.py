import json

main_data = {}
recipes_list = []
ingredients_list = []


def take_recipe():
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
    # print("🔎 Current object preview:", main_data)

def checking_user():
    user_input = input("Do you want to add a recipe? (yes/no): ").strip().lower()
    if user_input == 'yes':
        recipes_num = int(input("How many recipes do you want to add? "))
        for i in range(recipes_num):
            print(f"Entering details for recipe {i + 1}:")
            take_recipe()
        checked = 1
        return checked 
    elif user_input == 'no':
        print("Exiting the Recipe App. Goodbye!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        checking_user()

def calc_difficult():
    for recipe in recipes_list:
        if recipe["Cooking Time (Minutes)"] < 10 and len(recipe["Ingredients"]) < 4:
            # print(f"{recipe['name']} is an easy recipe.")
            recipe["Difficulty"] = "Easy"
        elif recipe["Cooking Time (Minutes)"] < 10 and len(recipe["Ingredients"]) >= 4:
            # print(f"{recipe['name']} is a medium recipe.")
            recipe["Difficulty"] = "Medium"
        elif recipe["Cooking Time (Minutes)"] >= 10 and len(recipe["Ingredients"]) < 4:
            # print(f"{recipe['name']} is a intermediate recipe.")
            recipe["Difficulty"] = "Intermediate"
        elif recipe["Cooking Time (Minutes)"] >= 10 and len(recipe["Ingredients"]) >= 4:
            # print(f"{recipe['name']} is a hard recipe.")
            recipe["Difficulty"] = "Hard"
    # print("🔎 Current object preview with Difficulty levels:", recipes_list)
       
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

def load_file():
    file_path = input("Enter the path to the data file: ")
    global recipes_list, ingredients_list
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No saved data found.")
    except Exception as e:
        print("An error occurred while loading the data. Starting fresh.")
        print("Error details:", e)
    finally:
        main_data = data
        recipes_list = data["recipes_list"]
        ingredients_list = data["all_ingredients"]
        # print("📦 Recipes List:", main_data['recipes_list'])
        # print("🥕 Ingredients List:", ingredients_list)
def save_file():
    try:
        with open('data.txt', 'w') as f:
            json.dump(main_data, f)
        print("Data saved to data.txt")
    except Exception as e:
        print("An error occurred while saving the data.")
        print("Error details:", e)
    finally:
        print("Exiting the Recipe App. Goodbye!")

print("Welcome to the Recipe App!")
load_file()
checked = checking_user()
if checked :
    calc_difficult()
    showing_recipes()
    showing_ingredients()
    save_file()


