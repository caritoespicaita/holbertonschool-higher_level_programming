#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle():
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        """ instantiation """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        """ to set width - defines value of class rectangle width """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
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
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__width * self.__height
    
    def perimeter(self):
        """ return the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.__width + self.__height + self.__width + self.__height
