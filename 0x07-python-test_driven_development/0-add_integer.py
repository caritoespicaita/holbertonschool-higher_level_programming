#!/usr/bin/python3
""" this fuction adds two  numbers """


def add_integer(a, b=98):

    """ this fuction adds two  integers """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(a, float):
        b = int(b)

    return (a + b)
