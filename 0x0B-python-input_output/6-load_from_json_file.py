#!/usr/bin/python3#
""" function that that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """ create json to file """
    with open(filename, mode="w", encoding="utf-8") as json_file:
        json_string = json.load(my_obj)
        json_file.write(json_string)
