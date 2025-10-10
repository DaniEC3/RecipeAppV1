class Recipe:
  all_ingredients = []
  difficulty = ""
  def __init__(self,name,cooking_time):
    self.name = name
    self.cooking_time = cooking_time
    
  def calculate_difficulty(self):
    if self.cooking_time < 10 and len(self.ingredients) < 4:
      self.difficulty = "Easy"
    elif self.cooking_time < 10 and len(self.ingredients) >= 4:
      self.difficulty = "Medium"
    elif self.cooking_time >= 10 and len(self.ingredients) < 4:
      self.difficulty = "Intermediate"
    elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
      self.difficulty = "Hard"
    return self.difficulty
  def add_ingredient(self,*arg):
    for ingredient in arg:
      self.ingredients.append(ingredient)

  def get_ingredients(self):
    return self.ingredients
  
  # Method that works on the class instead of an instance
  @classmethod
  def update_all_ingredients(cls, new_ingredients):
      for ingredient in new_ingredients:
          if ingredient not in cls.all_ingredients:
              cls.all_ingredients.append(ingredient)

  def search_ingredient(self,ingredient):
    if ingredient in self.ingredients:
      return True
    else:
      return False
  
  def __str__(self):
    return f"Recipe for {self.name}. Cooking time: {self.cooking_time} minutes. Difficulty: {self.calculate_difficulty()}. Ingredients: {', '.join(self.ingredients)}"


recipe1 = Recipe("Pancakes",15)
recipe1.add_ingredient("Flour","Eggs","Milk","Sugar")

print(recipe1.get_ingredients())
    