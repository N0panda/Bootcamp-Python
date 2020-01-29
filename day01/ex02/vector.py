# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 20:30:19 by ythomas           #+#    #+#              #
#    Updated: 2019/11/06 14:15:12 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Vector:
    def __init__(self, param):
        self.param = param
        self.values = self.get_value(param, [])
        self.length = len(self.values)

    def get_value(self, param, value):
        if (isinstance(param, int) == 1):
            for i in range(param):
                value.append(i * 1.0)
        elif (isinstance(param, list) == 1):
            for i in param:
                if (isinstance(i, float) != 1): print("Values of the list has to be float"); sys.exit()
            value = param
        elif (isinstance(param, tuple) == 1):
            if (len(param) != 2): print ("range is formated as (float.float)"); sys.exit()
            for i in param:
                if isinstance(i, float) == 0: print ("range is formated as (float.float)"); sys.exit()
            i = param[0]; j = param[1];
            for iteration in range(int(i), int(j)):
                value.append(iteration * 1.0)
        else:
            print("Param hs to be [int | list of float | range of float]")
            sys.exit()
        return value

    def __add__(self, nb):
        i = 0
        if isinstance(nb, float) == 0 and isinstance(nb, int) == 0:
            print ("can't add a ", type(nb), "to a float"); sys.exit()
        while i < self.length:
            self.values[i] += float(nb)
            i += 1
        return self

    def __radd__(self, nb):
        i = 0
        if isinstance(nb, float) == 0 and isinstance(nb, int) == 0:
            print ("can't add a ", type(nb), "to a float"); sys.exit()
        while i < self.length:
            self.values[i] += float(nb)
            i += 1
        return self

    def __sub__(self, nb):
        i = 0
        if isinstance(nb, float) == 0 and isinstance(nb, int) == 0:
            print ("can't sub a ", type(nb), "to a float"); sys.exit()
        while i < self.length:
            self.values[i] -= float(nb)
            i += 1
        return self

    def __rsub__(self, nb):
        i = 0
        if isinstance(nb, float) == 0 and isinstance(nb, int) == 0:
            print ("can't sub a ", type(nb), "to a float"); sys.exit()
        while i < self.length:
            self.values[i] -= float(nb)
            i += 1
        return self
    def __truediv__(self, nb):
        i = 0
        if isinstance(nb, float) == 0 and isinstance(nb, int) == 0:
            print ("can't add a ", type(nb), "to a float"); sys.exit()
        if (nb == 0) : print("cant div by 0"); sys.exit();
        while i < self.length:
            self.values[i] /= float(nb)
            i += 1
        return self

    def __rtruediv__(self, nb):
        i = 0
        if isinstance(nb, float) == 0 and isinstance(nb, int) == 0:
            print ("can't add a ", type(nb), "to a float"); sys.exit()
        if (nb == 0) : print("cant div by 0"); sys.exit();
        while i < self.length:
            self.values[i] /= float(nb)
            i += 1
        return self

    def __str__(self):
        text = "Values : " + ", ".join(str(i)for i in self.values)
        return (text)

    def __repr__(self):
        text = "length of Vector = " + str(self.length) + " /// " +self.__str__()
        return (text)
