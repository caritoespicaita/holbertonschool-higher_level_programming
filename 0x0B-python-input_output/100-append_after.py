#!/usr/bin/python3#
""" function that that inserts a line of text to a file """


def append_write(filename="", text=""):
    """ after each line insert a specific sttring """
    with open(filename, mode="r", encoding="utf-8") as file:
        line_list = []
        while True:
            line = file.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(line_list)
