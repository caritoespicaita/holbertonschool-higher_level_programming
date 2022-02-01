#!/usr/bin/python3
"""
This module contains the function inherits_from
"""


def inherits_from(obj, a_class):
    """  returns True if the object is an instance 
    of a class that inherited (directly or indirectly) 
    from the specified class ; otherwise False.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
