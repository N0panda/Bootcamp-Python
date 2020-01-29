# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/18 16:40:32 by ythomas           #+#    #+#              #
#    Updated: 2019/11/18 17:21:00 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import pandas

class FileLoader:
    
    def load(path):
        mf = pandas.read_csv(path); print("Loading DataSet of", mf.shape)
        return mf

    def display(df, n = 0):
        if n >= 0:print(df.head(n))
        else: print(df.tail(n * -1))

myfile = FileLoader.load("athlete_events.csv")
FileLoader.display(myfile, 10)
FileLoader.display(myfile, -10)

