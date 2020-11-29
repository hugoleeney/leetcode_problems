"""
166. Fraction to Recurring Decimal
Medium

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.



Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
Example 4:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
Example 5:

Input: numerator = 1, denominator = 5
Output: "0.2"


Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
"""


class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:

        result = ""
        minus = True if n * d < 0 else False

        n = -n if n < 0 else n
        d = -d if d < 0 else d

        q = n // d
        r = n % d
        result += str(q)
        if r == 0:
            return "-" + result if minus else result

        result += "."

        n = r * 10

        record = {}  # {(n,r): position}

        while r > 0:
            q = n // d
            r = n % d

            if (n, r) in record:
                pos = record[(n, r)]
                r = result[:pos] + '(' + result[pos:] + ')'
                return "-" + r if minus else r

            result += str(q)
            record[(n, r)] = len(result) - 1

            n = r * 10

        return "-" + result if minus else result


if __name__ == "__main__":

    s = Solution()
    s.fractionToDecimal(2,1) == "2"
    s.fractionToDecimal(1,2) == "0.5"
    s.fractionToDecimal(4,333) == "0.(012)"