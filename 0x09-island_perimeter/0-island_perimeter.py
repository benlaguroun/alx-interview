#!/usr/bin/python3

""" Function to find perimiter of an island """
def island_perimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell contributes 4 edges to the perimeter

                # Check adjacent cells (up, down, left, and right)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # If the upper neighbor is also land, subtract 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # If the left neighbor is also land, subtract 2

    return perimeter

# Example usage:
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12

