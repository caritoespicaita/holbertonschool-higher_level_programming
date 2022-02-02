#!/usr/bin/python3#
""" function that that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """ create json to file """
    with open(filename, mode="r") as json_file:
        return json.load(json_file)        
