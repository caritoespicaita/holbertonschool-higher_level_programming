#!/usr/bin/python3
""" Class Base """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):

        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method tha returns the JSON
        string representation list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method  that writes the JSON string
        representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(cls.to_json_string(
                            [item.to_dictionary() for item in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """static method tha returns the JSON
        string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  class method that returns an
            instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1)
        if cls.__name__ == "Square":
            dummy = Square(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ class method that returns a list of instances """
        try:
            filename = cls.__name__ + ".json"
            with open(filename, mode="r") as file:
                read_file = file.read()
                list_dict = cls.from_json_string(read_file)
                list = []
                for lists in list_dict:
                    list.append(cls.create(**lists))
                return list
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """that serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])
