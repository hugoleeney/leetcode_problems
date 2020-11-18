from itertools import chain
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return list(chain.from_iterable( [nums[i + 1]] * nums[i] for i in range(0, len(nums), 2)))


if __name__ == "__main__":
    s = Solution()
    r = s.decompressRLElist([1,2,3,4])
    assert r == [2,4,4,4]