"""
463. Island Perimeter
Difficulty: Easy


You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4


Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
"""
from typing import List


def do(grid, r, c, visited):
    if not grid[r][c]:
        return 0

    visited.add((r, c))

    dirs = [1, 1, 1, 1]
    mine = 0
    if r == 0 or not grid[r - 1][c]:
        mine += 1
        dirs[3] = 0
    if r == len(grid) - 1 or not grid[r + 1][c]:
        mine += 1
        dirs[1] = 0
    if c == 0 or not grid[r][c - 1]:
        mine += 1
        dirs[2] = 0
    if c == len(grid[0]) - 1 or not grid[r][c + 1]:
        mine += 1
        dirs[0] = 0

    for go, (dr, dc) in zip(dirs, ((0, 1), (1, 0), (0, -1), (-1, 0))):
        if go and (r + dr, c + dc) not in visited:
            mine += do(grid, r + dr, c + dc, visited)
    return mine


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        found = False
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    found = True
                    break
            if found:
                break
        return do(grid, r, c, set())


if __name__ == "__main__":
    s = Solution()
    assert s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
