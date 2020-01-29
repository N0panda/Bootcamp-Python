# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/09 13:30:45 by ythomas           #+#    #+#              #
#    Updated: 2019/11/09 17:18:09 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

class NumPyCreator:
    
    def from_list(self, lst):
        self.arr = np.array(lst)

    def from_tuple(self, tpl):
        self.arr = np.array(tpl)

    def from_iterable(self, itr):
        self.arr = np.array(itr)

    def from_shape(self, shape, value=0):
        self.arr = np.full(shape, value); 

    def random(self, shape):
        self.arr = np.random.uniform(size=shape)
    def identity(self, n):
        self.arr = np.identity(n)

    def __init__(self):
        pass
