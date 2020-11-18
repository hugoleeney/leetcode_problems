"""
1512. Number of Good Pairs
Difficulty: easy

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
"""
from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        good_ones = 0
        for k,v in c.items():
            good_ones += ((v-1) * v)/2
        return int(good_ones)


if __name__ == "__main__":
    s = Solution()
    assert s.numIdenticalPairs([1,2,3,1,1,3]) == 4