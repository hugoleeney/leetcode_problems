"""
1395. Count Number of Teams
Difficulty: medium

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).
"""
from itertools import combinations as combs
from itertools import chain
from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return sum( chain.from_iterable((c[0] < c[1] and c[1] < c[2], c[0] > c[1] and c[1]> c[2]) for c in combs(rating, 3)))


if __name__ == "__main__":
    s = Solution()
    assert s.numTeams([2,5,3,4,1]) == 3
