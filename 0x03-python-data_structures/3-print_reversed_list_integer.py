#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for list in range(len(my_list)):
        my_list = my_list[::-1]
        print("{:d}".format(my_list[list]))
