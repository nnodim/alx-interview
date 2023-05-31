#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner between Maria and Ben
    based on the results of playing a game.
    """
    winner_counter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        round_winner = isRoundWinner(nums[i], x)
        if round_winner is not None:
            winner_counter[round_winner] += 1

    if winner_counter['Maria'] > winner_counter['Ben']:
        return 'Maria'
    elif winner_counter['Ben'] > winner_counter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    """
    Determines the winner of a game where
    two players take turns removing numbers from a list.
    """
    numbers = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        current_player = players[i % 2]
        selected_ids = []
        prime = -1

        for idx, num in enumerate(numbers):
            if prime != -1:
                if num % prime == 0:
                    selected_ids.append(idx)
            else:
                if isPrime(num):
                    selected_ids.append(idx)
                    prime = num

        if prime == -1:
            return players[1] if current_player == players[0] else players[0]
        else:
            for idx, val in enumerate(selected_ids):
                del numbers[val - idx]

    return None


def isPrime(n):
    """
    Determines if a given integer is prime.
    """
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return "Not prime"
        return True
