all_recipes = []
recipe_1 = {"name": " Tea","Cooking Time (Minutes)": 5, "Ingredients": ("Tea Leaves","Sugar","Water")}
recipe_2 = {"name": "Pasta", "Cooking Time (Minutes)": 15, "Ingredients": ("Pasta", "Salt", "Olive Oil")}
recipe_3 = {"name": "Omelette", "Cooking Time (Minutes)": 10, "Ingredients": ("Eggs", "Salt", "Pepper")}
recipe_4 = {"name": "Salad", "Cooking Time (Minutes)": 8, "Ingredients": ("Lettuce", "Tomato", "Cucumber")}
recipe_5 = {"name": "Rice", "Cooking Time (Minutes)": 20, "Ingredients": ("Rice", "Water", "Salt")}


# all_recipes.append(recipe_1)
all_recipes.extend([recipe_1, recipe_2, recipe_3, recipe_4, recipe_5])

for recipe in all_recipes:
    print(recipe['Ingredients'])
# print(all_recipes)
# print(all_recipes[1].get("ingredients")[1])