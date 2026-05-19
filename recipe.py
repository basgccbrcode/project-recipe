class Recipe:
    def __init__(self, name, ingredients, instructions, category, rating):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.time = time
        self.temp = temp
        self.category = category
        self.rating = rating

        # bas' updates, change back if conflict

#----------------------

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

<<<<<<< HEAD
def Breakfast(self, category):
    print("Recipe for breakfast")

def Lunch(self, category):
    print("Recipe for lunch")
=======
    # Homework: to be continued...
#recipe_list[Recipe(field, field, field), Recipe(field, field, field)]
#recipe_list.append(Recipe(Field, field etc))
#for Recipe in recipe_list
    #print Recipe.name    
>>>>>>> 301a3b68dfdf61296ba92f932f02cbf21ffcf27c
