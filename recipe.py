class Recipe:
    def __init__(self, name, ingredients, instructions, time, temp, category, rating):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.rating = rating
        self.time = time
        self.temp = temp
#Michael's Changes feel free to change back if needed

def receipe_name(self, name):
    self.name = name

def time_num(self, time):
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

    self.instructions = print(f"preheat oven to {temperature_num}, mix ingredients, bake for {time_num} minutes")

    # Homework: to be continued...
#recipe_list[Recipe(field, field, field), Recipe(field, field, field)]
#recipe_list.append(Recipe(Field, field etc))
#for Recipe in recipe_list
    #print Recipe.name 




"""
Search and Organization:
#matches = [r for r in recipe_list if r.name == recipeA]
#print([r.name for r in matches])

"""
