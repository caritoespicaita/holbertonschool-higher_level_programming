#!/usr/bin/python3
""" Class rectangle inherits fron Base """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """method getter, get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """method setter, set value of width"""
        if(type(value) != int):
            raise TypeError("width must be an integer")
        elif(value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """method getter, get value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """method setter, set value of height"""

        if(type(value) != int):
            raise TypeError("height must be an integer")
        elif(value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """method getter, get value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """method setter, set value of x"""

        if(type(value) != int):
            raise TypeError("x must be an integer")
        elif(value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """method getter, get value of y"""
        return self.__y

    @y.setter
    def y(self, value=0):
        """method setter, set value of y"""

        if(type(value) != int):
            raise TypeError("y must be an integer")
        elif(value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ returns the area value of the Rectangle """
        return self.__width * self.__height

    def display(self):
        """method for print square whit #"""
        print(self.__y * "\n", end="")
        for x in range(self.__height):
            print((" " * self.__x) + (self.__width * "#"))

    def __str__(self):
        """ method than returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        p_id = self.id
        p_x = self.__x
        p_y = self.__y
        p_w = self.__width
        p_h = self.__height
        mge = "[Rectangle] ({}) {}/{} - {}/{}".format(p_id, p_x, p_y, p_w, p_h)
        return mge

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute"""
        arg = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, arg[i], value)

        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returns the
        dictionary representation of a Rectangle"""
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "width": self.__width, "height": self.__height}

