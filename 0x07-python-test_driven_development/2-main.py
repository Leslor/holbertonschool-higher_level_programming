#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided


matrix = [
    [1, -2, 4],
    [4, 3.5, -7],
    [21, 1, 3]
    ]


print(matrix_divided(matrix, float('nan')))
print(matrix_divided(matrix, float('inf')))

