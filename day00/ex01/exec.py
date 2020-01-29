# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 11:42:44 by ythomas           #+#    #+#              #
#    Updated: 2019/11/04 14:47:24 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

i = 1
my_list = []
if (len(sys.argv) > 1):
    while i < len(sys.argv):
        my_list.append(sys.argv[i])
        i += 1
        string = " ".join(my_list)
    rev_str = (string[::-1]).swapcase()
    print (rev_str)
