class Recipe:
    def __init__(self, name, ingredients, instructions, time, temp, category, rating):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.time = time
        self.temp = temp
        self.category = category
        self.rating = rating

        # bas' updates, change back if conflict

def receipe_name(self, name):
    self.name = name
def time_to_cook(self, time):
    self.time = time

def temp_num(self, temp):
    self.temp = temp

def receipe_ingredients(self, ingredients):
    print(f"Recipe: {self.name}")
    print(f"Time: {self.time}")
    print("Ingredients:")
    for ingredient in self.ingredients:
        print(f"- {ingredient}")
    self.ingredients += ingredients
    self.instructions = print(f"preheat oven to {temp_num}, mix ingredients, bake for {time_to_cook} minutes")

def Breakfast(self, category):
    print("Recipe for breakfast")

def Lunch(self, category):
    print("Recipe for lunch")

def Dessert(self, category):
    print("Custard or another recipe?")

class MealMapCore:
    def __init__(self):
        self.recipe_list = []

    def add_recipe(self, recipe):
        self.recipe_list.append(recipe)

    def remove_recipe(self, index):
        self.recipe_list.pop(index)

    def read_recipe(self, index):
        r = self.recipe_list[index]
        print(r.name, r.ingredients)

    def read_recipe_names(self):
        for r in self.recipe_list:
            print(r.name)

    def search(self, name):
        matches = [r for r in self.recipe_list if r.name.lower() == name.lower()]
        return matches





"""
Search and Organization:
#matches = [r for r in recipe_list if r.name == recipeA]
#print([r.name for r in matches])

"""
