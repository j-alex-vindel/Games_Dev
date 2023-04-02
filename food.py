class Food:
    def __init__(self,name,carbs,protein,fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def tot_calories(self):
        return self.carbs*4 + self.protein*4 + self.fat*9

class Recipe:
    def __init__(self,name,ingredients):
        self.name = name
        self.ingredients = ingredients
    def __str__(self):
        return self.name

    def calories(self):
        total = 0
        for ingredient in self.ingredients:
            total = total + ingredient.tot_calories()
        return total

pbj = Recipe('Peanut Butter & Jelly',[Food('Peanut Butter',6,8,16),
                                      Food('Jelly',13,0,0),
                                      Food('Bread',6,7,2)])

omelette = Recipe('Omelette du Fromage',[Food('Eggs',3,18,15),
                                         Food('Cheese',5,24,24)])

recipes = [pbj,omelette]

for recipe in recipes:
    print('{}: {} calories'.format(recipe.name,recipe.calories()))
