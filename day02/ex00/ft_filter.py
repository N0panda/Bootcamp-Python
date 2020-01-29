# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 17:28:44 by ythomas           #+#    #+#              #
#    Updated: 2019/11/06 19:38:10 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string

def ft_filter(function_to_apply, list_of_inputs):
    for line in list_of_inputs:
        if(function_to_apply(line) == True): yield line


##############################################################
#def lower(s):
#    if(s.islower() == 1):return (True)
#    else: return(False)
#def positif(x):
#    if(x >= 0): return (True)
#    else: return (False)
#
#text = ["AAAAA", "aaaaa", "AaAaAa", "aaaAaaa"]
#test2 = ["AAAAA", "aaaaa", "AaAaAa", "aaaAaaa"]
#
#number = (10, 9, -1, -5, 8, 45, 78, -8, 0, -0)
#number2 = (10, 9, -1, -5, 8, 45, 78, -8, 0, -0)
#
# print (list(filter(lower, text)))
# print (list(ft_filter(lower, test2)))
# print (list(filter(positif, number)))
# print (list(ft_filter(positif, number2)))
#
###############################################################
