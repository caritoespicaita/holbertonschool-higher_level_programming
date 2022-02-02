#!/usr/bin/python3
""" script that adds all arguments to a Python list,
and then save them to a file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except Exception:
    my_list = []

if len(sys.argv) > 1:
    for iterador in range(1, len(sys.argv)):
        my_list.append(sys.argv[iterador])
save_to_json_file(my_list, "add_item.json")
