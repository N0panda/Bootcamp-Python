# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 20:30:12 by ythomas           #+#    #+#              #
#    Updated: 2019/11/06 14:15:16 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

v1 = Vector(5)
v2 = v1 - 5
print (v1.values)
v1 = Vector(5)
v2 = v1 / 2
print (v1.values)
v1 = Vector(5)
v2 = 2 / v1 
print (v1.values)
print(v1.__repr__())
