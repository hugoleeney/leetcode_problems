"""
349. Intersection of Two Arrays
Easy
"""
from typing import List



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = set()

        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.intersection([1,2,2,1], [2,2]) == set([2]), s.intersection([1,2,2,1], [2,2])
