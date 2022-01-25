#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle():
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ instantiation """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """ print the rectangle whit # """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            str(self.print_symbol) * self.__width for i in range(self.__height)
            )

    def __repr__(self):
        """ print instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete Rectangle"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area:
            return rect_1
        else:
            return rect_2
