#!/usr/bin/python3
"""
This program solves the N queens problem using backtracking
"""
import sys


def safe(board, row, col):
    """
    Check if a position is safe
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def solve(board, col):
    """
    Solve the problem using backtracking
    """
    if col == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return True
    res = False
    for i in range(N):
        if safe(board, i, col):
            board[i][col] = 1
            res = solve(board, col + 1) or res
            board[i][col] = 0
    return res


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for i in range(N)] for j in range(N)]

    solve(board, 0)
