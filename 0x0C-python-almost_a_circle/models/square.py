#!/usr/bin/python3
""" Class rectangle inherits 
fron Rectangle 
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """method getter, get value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """method setter, set value of size"""
        self.width = value
        self.height = value
    
    def __str__(self):
        """ method than returns
        [Square] (<id>) <x>/<y> - <size>
        """
        p_id = self.id
        p_x = self.x
        p_y = self.y
        p_s = self.width
        mge = "[Square] ({}) {}/{} - {}".format(p_id, p_x, p_y, p_s)
        return mge
    
    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute"""
        arg = ["id", "size", "x", "y"]
        for i, value in enumerate(args):
            setattr(self, arg[i], value)
        
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ method that returns the 
        dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, 
                "size": self.size, "y": self.y}