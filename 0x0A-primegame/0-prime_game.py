#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner between Maria and Ben
    based on the results of playing a game.
    """
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for n in nums:
        roundWinner = isRoundWinner(n)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n):
    """
    Determines the winner of a game where
    two players take turns removing numbers from a list.
    """
    numbers = list(range(1, n + 1))
    players = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1

        for idx, num in enumerate(numbers):
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            else:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num

        if prime == -1:
            return players[1] if currentPlayer == players[0] else players[0]
        else:
            for idx, val in enumerate(selectedIdxs):
                del numbers[val - idx]

    return None


def isPrime(n):
    """
    Determines if a given integer is prime.
    """
    if n < 2 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
