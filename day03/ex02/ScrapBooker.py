# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/09 18:03:57 by ythomas           #+#    #+#              #
#    Updated: 2019/11/18 14:38:51 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.image as mpimg
import numpy as np
import sys

class ScrapBooker:
    
    def crop(array, dimensions, position):
        height = len(array)
        width = len(array[0])
        if dimensions[0] > width or dimensions[1] > height: print("error"); sys.exit()
        result = array[position[0]:position[0] + dimensions[0], position[1]:position[1] + dimensions[1]]
        return result

    def thin(array, n, axis):
        return np.delete(array, np.s_[::n], axis)
   
    def juxtapose(array, n, axis):
        result = array
        for nb in range(1, n):
            result = np.concatenate((array, result), axis)
        return result

    def mosaic(array, dimensions):
        tmp = ScrapBooker.juxtapose(array, dimensions[0], 0)
        result = ScrapBooker.juxtapose(tmp, dimensions[1], 1)
        return result
        
img = mpimg.imread("test.png")
#image = ScrapBooker.crop(img, [500, 500], [400, 400])
#image = ScrapBooker.thin(img, 2, 0)
#image = ScrapBooker.juxtapose(img, 2, 0)
image = ScrapBooker.mosaic(img, [5, 5])
mpimg.imsave("result.png", image)
