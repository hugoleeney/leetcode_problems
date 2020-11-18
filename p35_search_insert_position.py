'''
35. Search Insert Position

Difficulty: easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums)
        while True:
            if s == e:
                return s

            search_at = ((e - s) // 2) + s

            if nums[search_at] < target:
                s = search_at + 1
            elif nums[search_at] > target:
                e = search_at
            else:
                return search_at


if __name__ == "__main__":
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    r = s.searchInsert(nums, target)
    assert r == 4
