"""
1281. Subtract the Product and Sum of Digits of an Integer
Difficulty: Easy

Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = 1
        product = 1
        sumy = 0
        while m <= n:
            digit = ((n % (m * 10)) - sumy) // m
            product *= digit
            sumy += digit
            m *= 10
        return product - sumy


if __name__ == "__main__":
    s = Solution()
    assert s.subtractProductAndSum(1) == 0
    assert s.subtractProductAndSum(2) == 0
    assert s.subtractProductAndSum(234) == 15
    assert s.subtractProductAndSum(4421) == 21