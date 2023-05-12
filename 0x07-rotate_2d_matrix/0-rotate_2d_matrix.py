#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    '''
    rotates a 2d matrix 90 degrees clockwise
    '''
    left = 0
    right = len(matrix) - 1

    while left < right:
        top = left
        bottom = right
        for i in range(right - left):
            top_left = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left
        right -= 1
        left += 1
