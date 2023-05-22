#!/usr/bin/python3
"""
0x08. Making Change
"""


def makeChange(coins, total):
    """
    Returns:
        int: Fewest number of coins needed.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        if total <= 0:
            break

        num_used = total // coin
        num_coins += num_used
        total -= (num_used * coin)

    if total != 0:
        return -1

    return num_coins
