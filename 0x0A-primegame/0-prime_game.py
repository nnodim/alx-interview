#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of a game based on a list of numbers.
    """
    def is_prime(n):
        """
        Determines whether a number is prime or not.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def remove_multiples(lst, num):
        """
        Removes all multiples of a given number from a list.
        """
        return [x for x in lst if x % num != 0]

    def play_game(lst):
        """
        This function takes a list of integers 'lst' as input
        and plays a game between Maria and Ben.
        """
        maria_turn = True
        while lst:
            prime_nums = [x for x in lst if is_prime(x)]
            if not prime_nums:
                break
            num = max(prime_nums)
            lst = remove_multiples(lst, num)
            maria_turn = not maria_turn
        return "Maria" if not maria_turn else "Ben"

    winners = []
    for i in range(x):
        lst = list(range(1, nums[i]+1))
        winners.append(play_game(lst))

    if winners.count("Maria") > winners.count("Ben"):
        return "Maria"
    elif winners.count("Maria") < winners.count("Ben"):
        return "Ben"
    else:
        return None
