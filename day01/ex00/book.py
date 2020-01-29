# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 18:20:08 by ythomas           #+#    #+#              #
#    Updated: 2019/11/05 19:46:33 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import datetime

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def check_params(self, name, last_update, creation_date, recipes_list):
        if (isinstance(name, str) == 0) or (len(name) <= 0):
            print("Bad [name] param"); exit.sys()
        if (isinstance(last_update, datetime) == 0):
            print("last_update has to be a Datetime type")
        if (isinstance(creation_date, datetime) == 0):
            print("creation_date has to be a Datetime type")
        if (isinstance(recipes_list, dict) == 0):
            print("recipes_list  has to be a Dict type")

    def get_recipe_by_name(self, name):
        i = 0
        while i < len(self.recipes_list):
            if (self.recipes_list[i].name == name):
                print(self.recipes_list[i])
            i += 1

    def get_recipes_by_types(self, recipe_type):
        i = 0
        while i < len(self.recipes_list):
            if (self.recipes_list[i].recipe_type == recipe_type):
                print(self.recipes_list[i])
            i += 1

    def add_recipe(self, recipe):
        self.recipes_list.append(recipe)
        self.last_update = datetime.datetime.now()
