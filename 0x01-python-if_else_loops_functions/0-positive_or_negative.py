#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    rta = "is positive"
    elif number == 0:
        rta = "is zero"
        else:
            rta = "is negative"
print("{:d}".format(number), rta)
