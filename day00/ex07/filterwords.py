# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/05 12:30:14 by ythomas           #+#    #+#              #
#    Updated: 2019/11/05 12:40:29 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 3: print("Bard Number of params"); sys.exit()
string = sys.argv[1]
if sys.argv[2].isdigit(): length = int(sys.argv[2])
else: print("Bad params"); sys.exit()
my_list = []
for word in string.split(' '):
    if len(word) > length: my_list.append(word)
print(my_list)
