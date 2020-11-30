"""
680. Valid Palindrome II
Easy

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
import math


class Solution:
    """
    Not a very good solution, there are less confusing ways of doing it.
    """
    def validPalindrome(self, s: str) -> bool:

        if len(s) % 2 == 0:
            a = s[:(len(s) // 2)]
            b = list(reversed(s[math.ceil(len(s) / 2):]))
        else:
            a = s[:(len(s) // 2) + 1]
            b = list(reversed(s[math.ceil((len(s) / 2) - 1):]))

        i = 0
        j = 0

        """
        if one string end up longer than the other we can ignore the last char of the longer string
        """
        fail_point = None
        fails = 0
        while True:
            if i >= len(a) or j >= len(b):
                return True

            if a[i] == b[j]:
                i += 1
                j += 1

            else:
                if fails == 1:
                    i = fail_point[0]
                    j = fail_point[1] + 1
                    fails += 1
                elif fails == 0:
                    fail_point = (i, j)
                    fails = 1
                    i += 1
                else:
                    return False


if __name__ == "__main__":
    s = Solution()
    assert s.validPalindrome("abca") == True