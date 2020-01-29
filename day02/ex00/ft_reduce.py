# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 19:38:30 by ythomas           #+#    #+#              #
#    Updated: 2019/11/06 20:17:18 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs):
    result = list_of_inputs[0]
    for i in range(1, len(list_of_inputs)):
        result = function_to_apply(result, list_of_inputs[i])
    return (result)

#################################################################
#product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
#product2 = ft_reduce((lambda x, y: x * y), [1, 2, 3, 4])
#print (product)
#print (product2)
################################################################
