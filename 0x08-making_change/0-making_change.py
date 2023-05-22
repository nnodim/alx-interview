#!/usr/bin/python3
"""
0x08. Making Change
"""
import sys


def makeChange(coins, total):
    """
    0. Change comes from within
    """
    if total <= 0:
        return 0

    min_num = [float('inf')] * (total + 1)
    min_num[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_num[i] = min(
                    min_num[i], 1 + min_num[i - coin])

    if min_num[total] == float('inf'):
        return -1

    return min_num[total]
