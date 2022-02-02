#!/usr/bin/python3
""" Class Student
"""


class Student():

    def __init__(self, first_name, last_name, age):
        """ Instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student """
        dictionary = dict()
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    dictionary[i] = self.__dict__[i]
            return dictionary

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        myList = json.items()
        myList = list(myList)
        dic = {}
        for i in myList:
            if i[0] in self.__dict__:
                self.__dict__[i[0]] = i[1]
        return self.__dict__
