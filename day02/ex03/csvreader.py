# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 15:55:11 by ythomas           #+#    #+#              #
#    Updated: 2019/11/08 18:28:08 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import os

class CsvReader:

    def __init__(self, sep=';', header=True, skip_top=0, skip_bottom=0):
        self.sep = sep
        self.header = header
        self.s_top = skip_top
        self.s_bot = skip_bottom

    def __enter__(self):
        try: self.my_file = open(sys.argv[1])
        except:
            if os.stat(self.my_file).st_size == 0: print("File is empty"); return (None)
            return (None)
        else:
            return (self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.my_file.close()

    def getdata(self):
        self.f = []
        if self.header == True: nb = 1; self.s_top += 1
        else: nb = 0
        for i in self.my_file.read().splitlines():
            self.f.append(i)
        arg = len(self.f[nb].split(self.sep))
        for j in self.f[self.s_top:(len(self.f) - self.s_bot)]:
            if (len(j.split(self.sep))) != arg: print("FILE IS CORRUPTED " + "[line : \n]", j, "\n", arg, len(j.split(self.sep)))

    def getheader(self):
        if self.header == False: return None
        else: print(self.f[0])

with CsvReader() as csv:
    data = csv.getdata()
    header = csv.getheader()


