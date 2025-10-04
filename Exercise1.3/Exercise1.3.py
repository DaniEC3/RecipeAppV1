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
        print(ingredient)
        print(ingredients_list)
        if ingredient not in ingredients_list:
            ingredients_list.extend([ingredient])
    print(f"Recipe '{recipe_name}' added successfully!")
    print("Current Recipes List:")
    for r in recipes_list:
        print(r)
    print("Current Ingredients List:")
    print(ingredients_list)

def checking_user():
    user_input = input("Do you want to add a recipe? (yes/no): ").strip().lower()
    if user_input == 'yes':
        recipes_num = int(input("How many recipes do you want to add? "))
        for i in range(recipes_num):
            print(f"Entering details for recipe {i + 1}:")
            take_recipe()
    elif user_input == 'no':
        print("Exiting the Recipe App. Goodbye!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        checking_user()

print("Welcome to the Recipe App!")

def recipes_list_for():
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

checking_user()
recipes_list_for()
showing_recipes()
showing_ingredients()


