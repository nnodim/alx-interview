#!/usr/bin/python3
"""
0x09. Island Perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    perimeter = 0
    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check top cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
