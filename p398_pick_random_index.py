"""
398. Random Pick Index
Medium

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = {}
        for idx, i in enumerate(nums):
            self.nums.setdefault(i, []).append(idx)

    def pick(self, target: int) -> int:
        print(self.nums)
        l = self.nums[target]
        return random.choice(l)
        out = random.choice(l)
        print(out)
        return out


if __name__ == "__main__":
    s = Solution()
    s.pick()
