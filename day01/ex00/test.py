# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 15:48:50 by ythomas           #+#    #+#              #
#    Updated: 2019/11/05 19:46:31 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe
import datetime

pizza = Recipe("pizza", 2, 20, ["pate", "tomate", "fromage"], "plat italien", "lunch")
pancake = Recipe("pancake", 2, 10, ["farine", "eau", "sirop"], "tasty", "dessert")
salade = Recipe("salade", 1, 0, ["salade", "tomate", "oignon", "oeuf", "pignon"], "rafraichissant", "starter")
oeuf = Recipe("oeuf", 3, 10, ["oeuf", "mayo"], "good", "lunch")
soupe = Recipe("soupe", 4, 40, ["eau", "legume", "pate"], "en hiver", "dinner")
miamo = Recipe("miamo", 1, 0, ["fruit", "oil", "noix", "citron", "graines"], "plat vege", "lunch")

my_list = [pizza, pancake, salade, oeuf, soupe, miamo]
test = Book("cook", datetime.datetime.now(), datetime.datetime.now(), my_list)

test.get_recipe_by_name("salade")
test.get_recipes_by_types("lunch")
pates = Recipe("pates", 5, 20, ["pates", "eau"], "basic", "dinner")
test.add_recipe(pates)
test.get_recipes_by_types("dinner")
