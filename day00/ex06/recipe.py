# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 20:19:39 by ythomas           #+#    #+#              #
#    Updated: 2019/11/05 13:27:04 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys
import os

def add_recipies(recipe, ingredients, meal, prep_time):
    string = ingredients.split(',')
    if (recipe in cookbook): print("recipe already exist in the cookbook"); sys.exit()
    cookbook[recipe] = {"ingredients":string, "meal":meal, "prep_time":prep_time}

        

def print_recipies(name):
    if (name in cookbook):
        print (name, "Ingredient :", ", ".join([str(i) for i in cookbook[name]["ingredients"]]))
        print ("\tMeal :", cookbook[name]["meal"])
        print ("\tprep_time :", cookbook[name]["prep_time"])

def del_recipies(name):
    if name in cookbook:
        cookbook.pop(name)
        print (name, "is removed")
    else:
        print (name, " Does not exist")

def print_book():
    for recipe in cookbook: print_recipies(recipe)

cookbook = {"sandwich": {"ingredients": ["hame", "bread", "cheese", "tomatoes"], "meal": "lunch", "prep_time": 60},
            "cake": {"ingredients": ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time": 60},
            "salad": {"ingredients": ["avocado", "argula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15}}

os.system('clear')
print("\n-----  Your CookBook  -----\n")
print_book()
press = ' '
while press != 'q':
    print("\nwhat do you want to do ?")
    print("1 - Display your cookbook")
    print("2 - Add a recipe")
    print("3 - Remove a recipe")
    print("4 - Display one recipe")
    print("q - exit")
    press = input()
    os.system('clear')
    if press == '1':
        print_book()
    elif press == '2':
        print ("please enter : Recipe")
        name = input()
        print ("please enter : Ingredients [..., ..., ...]")
        ing = input()
        print ("please enter : Meal")
        meal = input()
        print ("please enter : Preparation time")
        pt = input()
        if pt.isdigit():
            add_recipies(name, ing, meal, int(pt))
        else:
            print("Bad time")
    elif press == '3':
        print("Please entre the recipe that you want to Remove")
        name = input()
        del_recipies(name)
    elif press == '4':
        print("Please entre the recipe that you want to Display")
        name = input()
        print_recipies(name)

