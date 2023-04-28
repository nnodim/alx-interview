#!/usr/bin/python3
"""
This program solves the N queens problem using backtracking
"""
import sys


def chess_board(n: int):
    """
    N Queens
    """
    result = []

    def check_board(row, col, col_in_row):
        """Checks board"""
        for i in range(row):
            if row - i == abs(col - col_in_row[i]):
                return False
        return True

    def save_board(row, cols, col_in_row):
        """
        Saves the current state of the board
        """
        if row == n:
            con_result = []
            for i in range(n):
                temp_result = []
                for j in range(n):
                    if j == col_in_row[i]:
                        temp_result.append(i)
                        temp_result.append(col_in_row[i])
                        con_result.append(temp_result)
                if len(con_result) == n:
                    result.append(con_result)
                    temp_result, con_result = [], []

    def place_queen(row, cols, col_in_row):
        """
        Place queen
        """
        save_board(row, cols, col_in_row)
        for col in range(n):
            if cols[col] == 0 and check_board(row, col, col_in_row):
                cols[col] = 1
                col_in_row[row] = col
                place_queen(row + 1, cols, col_in_row)
                cols[col] = 0
    place_queen(0, [0]*n, [0]*n)
    return result


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solution = chess_board(n)
    for nqueen in solution:
        print(nqueen)
