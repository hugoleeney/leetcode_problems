"""
1637. Widest Vertical Area Between Two Points Containing No Points
Difficulty: medium


Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.
"""
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        return max( [ abs(point[0]-points[idx][0]) for idx, point in enumerate(points[1:]) ] )


if __name__ == "__main__":
    s = Solution()
    assert s.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]) == 1
    assert s.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]) == 3
