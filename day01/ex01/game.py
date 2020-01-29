# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 19:48:00 by ythomas           #+#    #+#              #
#    Updated: 2019/11/05 20:28:01 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = True

class Lanister(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lanister"
        self.house_word = "A Lanister always pay his debt"

    def print_house_words(self):
        print(self.house_word)

    def die(self):
        self.is_alive = False
