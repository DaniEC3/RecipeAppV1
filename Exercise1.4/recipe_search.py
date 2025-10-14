import pickle

def load_recipes():
    file_path = input("Enter the path to the data file: ")
    try:
        with open(file_path, "rb") as f:
            data = pickle.load(f)
    except FileNotFoundError:
        print("No saved data found.")
    except Exception as e:
        print("An error occurred while loading the data. Starting fresh.")
        print("Error details:", e)
    finally:
        return data["recipes_list"], data["all_ingredients"]

def display_recipe(recipes_list, all_ingredients):
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

def sorted_ingredients_list(all_ingredients):
    print("\nAvailable Ingredients List:")
    print("------------------------")
    sorted_ingredients = sorted(all_ingredients)
    index_ingredients = {}
    for i, ingredient in enumerate(sorted_ingredients, start=1):
        print(f"{i}. {ingredient}")
        index_ingredients[i] = ingredient
    print("------------------------\n")
    return index_ingredients

def search_ingredients(all_ingredients, recipes_list):
    index_ingredients = sorted_ingredients_list(all_ingredients)
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
    
def main():
    print("Welcome to the Recipe Search App!")
    recipes_list, all_ingredients = load_recipes()
    sorted_ingredients_list(all_ingredients)
    display_recipe(recipes_list,all_ingredients)
    search_ingredients(all_ingredients, recipes_list)
    print("Exiting the Recipe Search App. Goodbye!")
main()