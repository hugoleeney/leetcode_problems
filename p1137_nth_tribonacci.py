"""
p1137 nth tribonacci
Difficulty: easy

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""


class Solution:
    def tribonacci(self, n: int) -> int:

        a = 0
        b = 1
        c = 1

        if n < 3:
            return a if n == 0 else (b if n == 1 else c)

        i = 2

        trib = None

        while i < n:
            trib = a + b + c
            a = b
            b = c
            c = trib
            i += 1
        return trib


if __name__ == "__main__":
    s = Solution()
    s. tribonacci(0) == 0
    s. tribonacci(1) == 1
    s. tribonacci(2) == 1
    s. tribonacci(3) == 2
    s. tribonacci(4) == 4
    s. tribonacci(5) == 7