# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 14:48:39 by ythomas           #+#    #+#              #
#    Updated: 2019/11/04 15:24:09 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

if (len(sys.argv) != 2):
    print("Bad Number of param"); sys.exit()
if (sys.argv[1].isdigit() == 0):
    print("error"); sys.exit()
nb = int(sys.argv[1])
if (nb == 0):
    print ("I'm Zero")
elif (nb % 2 == 0):
    print ("I'm Even")
else:
    print ("I'm Odd")

