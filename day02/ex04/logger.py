# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ythomas <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 13:02:42 by ythomas           #+#    #+#              #
#    Updated: 2019/11/08 15:54:16 by ythomas          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import getpass
import time
import logging
from random import randint

logging.basicConfig(filename="machine.log", filemode="w" ,level=20)

def log(fonction):
    name = fonction.__name__
    def wrapper(*ac, **av):
        start = time.time()
        ret = fonction(*ac, **av)
        end = time.time()
        logging.info(getpass.getuser() + fonction.__name__ +"\t\t[ exec-time = {:.5} ms ]\
        ".format(str(end - start)))
        return (ret)
    return (wrapper)

class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
