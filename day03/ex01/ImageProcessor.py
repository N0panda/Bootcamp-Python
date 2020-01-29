# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/09 17:19:33 by ythomas           #+#    #+#              #
#    Updated: 2019/11/09 18:01:48 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from PIL import Image

class ImageProcessor:
    
    def load(path):
        im = Image.open(path)
        arr = np.array(im)
        print("Loading an image of dimensions : ",  arr.shape, "\n")
        return(arr)

    def display(array):
        new_image = Image.fromarray(array)
        new_image.save("test_transformed.png")

    def __init__(self):
        pass

var = ImageProcessor.load("./test.png")
ImageProcessor.display(var)
print(var)
