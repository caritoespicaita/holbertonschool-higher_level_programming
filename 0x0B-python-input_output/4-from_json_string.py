#!/usr/bin/python3#
""" function that returns returns an object  represented by a JSON string """
import json


def from_json_string(my_str):
    """ saving struct data whit json """
    return json.loads(my_str)
