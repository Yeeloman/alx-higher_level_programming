#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda row: [x ** 2 for x in row], matrix))
    return new_matrix
