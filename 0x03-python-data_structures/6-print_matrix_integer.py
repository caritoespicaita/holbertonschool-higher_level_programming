#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        space = ''
        for k in i:
            print('{}{:d}'.format(space, k), end='')
            space = ' '
        print('')
