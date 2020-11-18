"""
980. Unique Paths III
Difficulty: hard

On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
"""
from typing import List

from itertools import permutations as perm


class Solution:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        squares = 0
        start = None
        end = None
        for r, row in enumerate(grid):
            for c, sq in enumerate(row):
                if sq != -1:
                    squares += 1
                if sq == 0:
                    grid[r][c] = 3
                if sq == 1:
                    start = (r, c)
                if sq == 2:
                    end = (r, c)
        return self.up(grid, start, squares)

    def up(self, grid, position, num_squares, depth=0, count=0):
        if grid[position[0]][position[1]] == 2 and depth + 1 == num_squares:
            return 1

        grid[position[0]][position[1]] = -2

        east = position[1] + 1
        if east < len(grid[0]) and grid[position[0]][east] > 1:
            prev_value = grid[position[0]][east]
            count += self.up(grid, (position[0], east), num_squares, depth + 1)
            grid[position[0]][east] = prev_value

        west = position[1] - 1
        if west >= 0 and grid[position[0]][west] > 1:
            prev_value = grid[position[0]][west]
            count += self.up(grid, (position[0], west), num_squares, depth + 1)
            grid[position[0]][west] = prev_value

        north = position[0] + 1
        if north < len(grid) and grid[north][position[1]] > 1:
            prev_value = grid[north][position[1]]
            count += self.up(grid, (north, position[1]), num_squares, depth + 1)
            grid[north][position[1]] = prev_value

        south = position[0] - 1
        if south >= 0 and grid[south][position[1]] > 1:
            prev_value = grid[south][position[1]]
            count += self.up(grid, (south, position[1]), num_squares, depth + 1)
            grid[south][position[1]] = prev_value

        return count


if __name__ == "__main__":
    s = Solution()
    assert s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]) == 2
    assert s.uniquePathsIII([[0,0,0,0,0,1,0,0,0,0,0,2,-1,0,0,-1,0,0,-1,0]]) == 0
    assert s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]) == 4
    assert s.uniquePathsIII([[0,1],[2,0]]) == 0
    assert s.uniquePathsIII([[1,2]]) == 1