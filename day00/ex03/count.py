# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 15:25:23 by ythomas           #+#    #+#              #
#    Updated: 2019/11/04 18:29:21 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import fileinput
import string

def text_analyzer(text):
    tab = {"Uppercase": 0, "Lowercase": 0, "Spaces": 0, "Ponctuation": 0, "len": 0}
    for line in text:
        for c in line:
            tab["len"] += 1
            if (c.isupper()):
                tab["Uppercase"] += 1
            elif (c.islower()):
                tab["Lowercase"] += 1
            elif (c == ' '):
                tab["Spaces"] += 1
            elif (c in string.punctuation):
                tab["Ponctuation"] += 1
    for x in tab:
        print (x + " : " + str(tab[x]))

if (len(sys.argv) > 2):
    print("Bad file number"); sys.exit()

text = []
for line in fileinput.input():
    text.append(line.rstrip())
text_analyzer(text)
