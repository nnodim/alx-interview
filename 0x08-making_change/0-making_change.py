#!/usr/bin/python3
"""
0x08. Making Change
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a table to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
