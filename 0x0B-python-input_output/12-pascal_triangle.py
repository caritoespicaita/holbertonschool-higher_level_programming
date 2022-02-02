#!/usr/bin/python3
""" Fuction that represents the Pascal's triangle
"""


def pascal_triangle(n):
    """  returns a list of lists of integers
    representing the Pascals triangle of n
    """
    list_save = []
    if n <= 0:
        return list_save
    for x in range(n):
        list = []
        list.append(1)
        if x == 0:
            list_save.append(list)
            continue
        for y in range(1, x):
            try:
                list.append(list_save[x - 1][y - 1] + list_save[x - 1][y])
            except:
                continue
        list.append(1)
        list_save.append(list)

    return list_save
