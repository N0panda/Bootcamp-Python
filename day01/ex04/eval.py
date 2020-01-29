# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/06 15:27:39 by ythomas           #+#    #+#              #
#    Updated: 2019/11/06 16:07:52 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Evaluator:

    def zip_evaluate(self, words, coefs):
        if (len(words) != len(coefs)):
            return (-1)
        zipped = zip(words, coefs)
        nb = 0.0
        for line, ide in zipped:
            if (isinstance(ide, float) == 0): print ("Bad coefs"); sys.exit()
            nb += (len(line) * 1.0) * ide
        return nb

    def enumerate_evaluate(self, words, coefs):
        if (len(words) != len(coefs)):
            return (-1)
        zipped = zip(words, coefs)
        nb = 0.0
        for line, ide in zipped:
            if (isinstance(ide, float) == 0): print ("Bad coefs"); sys.exit()
            nb += (len(line) * 1.0) * ide
        return nb
