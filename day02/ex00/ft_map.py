# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 16:53:57 by ythomas           #+#    #+#              #
#    Updated: 2019/11/06 19:07:31 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, *list_of_inputs):
    zipped = zip(*list_of_inputs)
    for line in zipped:
        yield (function_to_apply(*line))

#################################################
##def addt(x, y, z):
##    return (x + y + z)
##
#def uppp(s, l):
#    return (s + l)
#
#list_numbers = [1, 2, 3, 4, 8]
#tuple_numbers = (5, 6, 7, 8)
#numbers = (1, 1, 1, 1, 1, 1, 1)
#
#test = ft_map(addt, list_numbers, tuple_numbers, numbers)
#iteree = map(addt, list_numbers, tuple_numbers, numbers)
#
#y = map(uppp, ["Hello", "comment", "faire"], "De la noche")
#x = ft_map(uppp, ["Hello", "comment", "faire"], "De la noche")
#
#for i in iteree:
#    print(i)
#print()
#for i in test:
#    print(i)
#print()
#for i in y:
#    print(i)
#print()
#for i in x:
#    print(i)
#################################################
