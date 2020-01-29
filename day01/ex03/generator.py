# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 14:16:26 by ythomas           #+#    #+#              #
#    Updated: 2019/11/06 15:26:58 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import random
import string

def generator(text, sep, option):
    if (isinstance(text, str) == 0): print("param 1 has to be str"); sys.exit()
    if (isinstance(sep, str) == 0): print("param 2 has to be str"); sys.exit()
    my_list = text.split(sep)
    if isinstance(option, str) and option == "shuffle":
        random.shuffle(my_list)
    elif isinstance(option, str) and option == "unique":
        my_list = list(dict.fromkeys(my_list))
    elif isinstance(option, str) and option == "ordered":
        my_list = sorted(my_list, key=str.lower)
    for line in my_list:
        yield line

text = "C'est pour tout les sang de leurs morts qui msont tombe dessus le djo le david et le HOFFMANE SES MORTS"

for word in generator(text, " ", "unique"):
    print (word)
