# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 13:35:56 by ythomas           #+#    #+#              #
#    Updated: 2019/11/05 13:57:15 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

number = random.randint(1, 99)
iteration = 0
print("Try to find the hidden number !!!\nPleae enter a number =)")
while (1):
    iteration += 1
    string = input()
    if (string.isdigit() == 1):
        nb = int(string)
        if nb == number:
            print("***** WELL DONE *****\n\n You did it in : ", iteration, "turn"); break
        elif nb < number:
            print("too low")
        elif nb > number:
            print("too high")
    else:
        print("This is not a number")
    
