class Recipe:
  all_ingredients = []
  difficulty = ""
  def __init__(self,name,cooking_time):
    self.name = name
    self.cooking_time = cooking_time
    
  def calculate_difficulty(self):
    if self.cooking_time < 10 and len(self.__class__.all_ingredients) < 4:
      self.difficulty = "Easy"
    elif self.cooking_time < 10 and len(self.__class__.all_ingredients) >= 4:
      self.difficulty = "Medium"
    elif self.cooking_time >= 10 and len(self.__class__.all_ingredients) < 4:
      self.difficulty = "Intermediate"
    elif self.cooking_time >= 10 and len(self.__class__.all_ingredients) >= 4:
      self.difficulty = "Hard"
    return self.difficulty
  
  @classmethod
  def add_ingredient(cls,*arg):
    for ingredient in arg:
        if ingredient not in cls.all_ingredients:
            cls.all_ingredients.extend([ingredient])
  
  @classmethod
  def get_ingredients(cls):
    return cls.all_ingredients
  
  # Method that works on the class instead of an instance
  @classmethod
  def update_all_ingredients(cls, new_ingredients):
      for ingredient in new_ingredients:
          if ingredient not in cls.all_ingredients:
              cls.all_ingredients.append(ingredient)

  def search_ingredient(self,ingredient):
    if ingredient in self.all_ingredients:
      return True
    else:
      return False
  
  def recipe_search(self,data,ingredient):
    for recipe in data:
      if recipe.search_ingredient(ingredient):
        print(recipe)

  def __str__(self):
    return f"Recipe for {self.name}. Cooking time: {self.cooking_time} minutes. Difficulty: {self.calculate_difficulty()}. Ingredients: {', '.join(self.all_ingredients)}"

tea = Recipe("Tea",5)
coffee = Recipe("Coffee",5)
cake = Recipe("Cake",50)
banana_Smoothie = Recipe("Banana Smoothie",10)

recipes_list = [tea,coffee,cake,banana_Smoothie]

tea.add_ingredient("Tea leaves","Water","Sugar")
coffee.add_ingredient("Coffee powder","Water","Sugar")
cake.add_ingredient("Flour","Sugar","Eggs","Butter","Baking powder","Milk")
banana_Smoothie.add_ingredient("Banana","Milk","Sugar","Ice")

print(tea)

Recipe.recipe_search(tea,recipes_list,"Sugar")
