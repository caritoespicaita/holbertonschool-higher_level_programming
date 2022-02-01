#!/usr/bin/python3
"""
Empty Class BaseGeometry
"""


class BaseGeometry:
    """ A class with public attribute area """
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value is not an integer """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{:s} must be greater than 0".format(name))
