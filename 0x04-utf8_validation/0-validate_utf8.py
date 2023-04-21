#!/usr/bin/python3
"""
0. UTF-8 Validation
"""


def validUTF8(data):
    """
    A method that determines if a given data set represents
    a valid UTF-8 encoding.
    """
    byte = 0
    for char in data:
        if byte == 0:
            if char >> 5 == 0b110 or char >> 5 == 0b1110:
                byte = 1
            elif char >> 4 == 0b1110:
                byte = 2
            elif char >> 3 == 0b11110:
                byte = 3
            elif char >> 7 == 0b1:
                return False
        else:
            if char >> 6 != 0b10:
                return False
            byte -= 1
    return byte == 0
