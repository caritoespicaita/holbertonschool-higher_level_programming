#!/usr/bin/python3#
""" function that returns the JSON representation of an object """
import json


def save_to_json_file(my_obj, filename):
    """ write json to file """
    with open(filename, mode="w", encoding="utf-8") as json_file:
        json_string = json.dumps(my_obj)
        json_file.write(json_string)
