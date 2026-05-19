class Recipe:
    def __init__(self, name, ingredients, instructions, category, rating):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.rating = rating

#----------------------

def receipe_name(self, name):
    self.name = name

def receipe_ingredients(self, ingredients):
    print(f"Recipe: {self.name}")
    print("Ingredients:")
    for ingredient in self.ingredients:
        print(f"- {ingredient}")
    self.ingredients += ingredients

    self.instructions = "preheat oven to temperature (what is that in celsius?), mix ingredients, bake for time minutes"

def Breakfast(self, category):
    print("Recipe for breakfast")

def Lunch(self, category):
    print("Recipe for lunch")
