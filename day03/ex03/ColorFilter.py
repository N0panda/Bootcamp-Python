# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/18 14:39:55 by ythomas           #+#    #+#              #
#    Updated: 2019/11/18 16:18:02 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
import matplotlib.image as mpi

class ColorFilter:

    def invert(array):
        return (array - 1) * -1

    def to_blue(array):
        arr = np.zeros((len(array), len(array[0]), 3))
        arr[:,:,2] = array[:,:,2]
        return (arr)

    def to_green(array):
        arr = np.zeros((len(array), len(array[0]), 3))
        arr[:,:,1] = array[:,:,1]
        return (arr)

    def to_red(array):
        arr = np.zeros((len(array), len(array[0]), 3))
        arr[:,:,0] = array[:,:,0]
        return (arr)

    def celluloid(array):
        arr = np.zeros((len(array), len(array[0]), 3))
        arr[:,:,0] = array[:,:,2]
        arr[:,:,1] = array[:,:,2]
        arr[:,:,2] = array[:,:,2]
        return (arr)

img = mpi.imread("test.png")
#tmp = ColorFilter.invert(img)
tmp = ColorFilter.celluloid(img)
mpi.imsave("result.png", tmp)
