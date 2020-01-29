# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 10:49:27 by ythomas           #+#    #+#              #
#    Updated: 2019/11/08 12:30:45 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def what_are_the_vars(*var, **kwargs):
    if not var: return None
    obj = ObjectC()
    for cpt, i in enumerate(var):
        setattr(obj, "var_%s" % str(cpt), i)
    for j in kwargs:
        try:
            getattr(obj, j)
        except:
            setattr(obj, j, kwargs[j])
        else:
            return (None)
    return (obj)

class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")
if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
