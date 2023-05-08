#!/usr/bin/python3
"""N Queens"""
import sys


def solution_generator(n):
    solutions = [[]]
    for row in range(n):
        solutions = set_queen(row, n, solutions)
    return solutions


def set_queen(row, n, prev_solutions):
    safe_positions = []
    for solution in prev_solutions:
        for col in range(n):
            if is_safe(row, col, solution):
                safe_positions.append(solution + [col])
    return safe_positions


def is_safe(row, col, solution):
    for q, x in enumerate(solution):
        if x == col or abs(row - q) == abs(col - x):
            return False
    return True


def create():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    x = create()
    solutions = solution_generator(x)
    for solution in solutions:
        print([[q, x] for q, x in enumerate(solution)])


if __name__ == '__main__':
    n_queens()
