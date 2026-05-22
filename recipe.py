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



                   #Saving all recipe to exterior file. WILL OVERWRITE ALL VALUES PREVIOUSLY STORED#
    def save_to_txt(self, filename="recipes.txt"):
        with open(filename, "w", encoding="utf-8") as f:  # "w" = overwrite
            for r in self.recipe_list:
                f.write(f"{r.name}|{','.join(r.ingredients)}|{r.instructions}|{r.category}|{r.rating}\n")
        print(f"Wrote {len(self.recipe_list)} recipes to {filename}")
"""
##############################################################################################
                                FRONT END
##############################################################################################
"""
def main():
   manager = RecipeManager()


    #adding bar values
   manager.recipe_list.append(
       Recipe("Chocolate Cake",
              ["flour", "sugar", "cocoa", "eggs"],
              "Preheat oven to 180C, mix ingredients, bake 30 minutes",
              "Dessert", 4.5)
   )

# User interface!
   while True:
       print("\n" + "="*30)
       print("RECIPE MANAGEMENT")
       print("="*30)
       print("1. View all recipes")
       print("2. View recipe details")
       print("3. Add recipe")
       print("4. Edit recipe")
       print("5. Remove recipe")
       print("6. Search")
       print("7. Quit")


       choice = input("\nChoose (1-7): ").strip()

#           Potential choices
       if choice == "1":
           manager.read_recipe_names()
       elif choice == "2":
           manager.read_recipe()
       elif choice == "3":
           manager.add_recipe()
       elif choice == "4":
           manager.edit_recipe()
       elif choice == "5":
           manager.remove_recipe()
       elif choice == "6":
           manager.search()
       elif choice == "7":
           print("Exiting!")
           break
       else:
           print("Invalid choice")


"""
Search and Organization:
#matches = [r for r in recipe_list if r.name == recipeA]
#print([r.name for r in matches])

"""
