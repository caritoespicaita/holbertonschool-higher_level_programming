#!/usr/bin/python3#
""" Fuction that reads writes a string to a text file """


def write_file(filename="", text=""):
    """ return the number of characters written """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
