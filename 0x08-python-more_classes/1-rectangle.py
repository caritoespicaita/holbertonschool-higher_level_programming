#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle():
    """class Rectangle"""

    def _init_(self, width=0, height=0):
        """ instantiation """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ to retrieve width """
        return self.__with

    @width.setter
    def width(self, value):
        """ to set width - defines value of class rectangle width """
        if type(value) != int:
            raise typeError('width must be an integer')
        if type(value) < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ to retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ to set height - defines value of class rectangle height """
        if type(value) != int:
            raise typeError('height must be an integer')
        if type(value) < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
    pass
