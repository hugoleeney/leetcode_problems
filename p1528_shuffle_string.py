"""
1528. Shuffle String

Difficulty: easy

Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.


"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [None] * len(s)
        for ch, i in zip(s, indices):
            result[i] = ch
        return "".join(result)


if __name__ == "__main__":
    s = Solution()
    s.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]) == "leetcode"