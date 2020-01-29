# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 15:54:01 by ythomas           #+#    #+#              #
#    Updated: 2019/11/05 18:19:57 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def check_params(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if (isinstance(name, str) == 0) or (len(name) <= 0):
            print("Bad [name] param"); sys.exit()
        if (isinstance(cooking_lvl, int) == 0) or cooking_lvl < 0 or cooking_lvl > 5:
            print("Cooking_lvl has to be [1...5]")
        if (isinstance(cooking_time, int) == 0) and (cooking_time < 0):
            print("Cooking_time has to be a positive number")
        if isinstance(ingredients, list) == 0 and isinstance(lingredients, str):
            print("ingredients has to be a list of string of ingredients")
        if (isinstance(description, str) == 0):
            print("Bad type for description, it should be a str")
        if (isinstance(recipe_type, str) == 0) or (recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert"):
            print("recipe type has tto be [starter, lunch, dessert]")

    def __str__(self):
        text = self.name + ", " + str(self.cooking_lvl) + ", " + str(self.
        cooking_time) + ", [" + (" ,".join([str(i) for i in self.ingredients])) + "], " + self.description + ", " + self.recipe_type
        return text
