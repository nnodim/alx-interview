#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""
def rotate_2d_matrix(matrix):
    """
    rotate a 2D array 90 degrees clockwise.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n // 2):
        matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
    return matrix
