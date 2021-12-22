#!/usr/bin/python3
sep = ", "
for number in range(0, 100):
    if number == 99:
        sep = "\n"
    print("{:d}".format(number), end=sep)
