#!/usr/bin/python3#
""" Fuction that reads a tex file """

def read_file(filename=""):
    """ open file and print """
    with open (filename) as f:
        read_data = f.read()
        print(read_data)
    f.closed
