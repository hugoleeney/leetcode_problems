'''
27. Remove Element

Difficulty - Easy


Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                j += 1
                i += 1
            else:
                j += 1
        return i


if __name__ == "__main__":
    s = Solution()
    r = s.removeElement([3,2,2,3])
    assert r == 1
    assert s == [2,2]
