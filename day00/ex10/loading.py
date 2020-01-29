# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 13:59:29 by ythomas           #+#    #+#              #
#    Updated: 2019/11/08 18:39:06 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import os

def ft_progress(lst):
    length = len(lst)
    for i in lst:
        nb = (i+1) * 100 / (length)
        os.system('clear')
        tmp = int(nb / 2)
        print("----- Loading Please Wait -----\n")
        string = tmp * '|' + (50 - tmp) * '.'
        print(string, nb)
        print("\n----- Loading Please Wait -----\n")
        yield i

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)

