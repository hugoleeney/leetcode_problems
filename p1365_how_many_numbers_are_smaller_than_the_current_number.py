"""
1364. How Many Numbers Are Smaller Than the Current Number

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.



Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        nums2 = [x for x in zip(nums, range(len(nums)))]
        nums2.sort(key=lambda x: x[0])

        i = 0
        prev = (-1, -1)
        result = [0] * len(nums)
        while i < len(nums2):
            e = nums2[i]
            if e[0] != prev[0]:
                result[e[1]] = i
            else:
                result[e[1]] = result[prev[1]]
            prev = e
            i += 1
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.smallerNumbersThanCurrent([8,1,2,2,3]) == [4,0,1,1,3]