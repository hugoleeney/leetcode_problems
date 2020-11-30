"""
238. Product of Array Except Self
Medium

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        df = {}

        db = {0: 1}

        def f(i):
            if i == len(nums):
                return 1
            if i in df:
                return df[i]
            else:
                r = nums[i] * f(i + 1)
                df[i] = r
                return r

        output = []
        for idx, i in enumerate(nums):
            backward = db[idx]
            output.append(backward * f(idx + 1))
            db[idx + 1] = backward * i
        return output


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]