"""
283. Move Zeroes
Difficulty: Easy
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        i = 0

        while i < len(nums):
            while i < len(nums):
                if nums[i] == 0:
                    break
                i += 1

            j = i + 1
            while j < len(nums):
                if nums[j] != 0:
                    break
                j += 1

            if j >= len(nums):
                return

            nums[i], nums[j] = nums[j], nums[i]

            i += 1



if __name__ == "__main__":
    s = Solution()
    a = [0, 1, 0, 3, 12]
    s.moveZeroes(a)
    assert a == [1,3,12,0,0], a
