#!/usr/bin/python3
"""
Class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Representation of a rectangle """
    def __init__(self, width, height):
        """ instation of the rectangle """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
