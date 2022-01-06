#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    j = 1
    i = 0
    for i in matrix:
        row = []
        for k in i:
            row.append(k * k)
        new_matrix.append(row)
    return new_matrix
