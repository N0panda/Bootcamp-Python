# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 17:44:12 by ythomas           #+#    #+#              #
#    Updated: 2019/11/04 18:05:01 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) != 3): print("Bad number of params"); sys.exit()
for argument in sys.argv[1:]:
    if (argument.isdigit() == 0): print("Bad params"); sys.exit()
nb_one = int(sys.argv[1])
nb_two = int(sys.argv[2])
print("Sum        :       "+ str(nb_one + nb_two))
print("Difference :       "+ str(nb_one - nb_two))
print("Product    :       "+ str(nb_one * nb_two))
if (nb_two == 0): print("Quotient   :        ERROR")
else:
    print("Quotient   :       "+ str(nb_one / nb_two))
if (nb_two == 0): print("Remainder  :        ERROR")
else:
    print("Remainder  :       "+ str(nb_one % nb_two))
