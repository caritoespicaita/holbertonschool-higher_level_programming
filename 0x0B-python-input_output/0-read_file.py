#!/usr/bin/python3#
""" Fuction that reads a tex file """


def read_file(filename=""):
    """ open file and print """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
