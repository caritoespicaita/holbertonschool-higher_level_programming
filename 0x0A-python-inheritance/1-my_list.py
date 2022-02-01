#!/usr/bin/python3
""" Class MyList"""


class MyList(list):
    """ a subclass of List """
    def __init__(self):
        """ initializes the object"""
        super().__init__()

    def print_sorted(self):
        """ print the sorted list """
        print(sorted(self))
