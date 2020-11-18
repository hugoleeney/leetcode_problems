"""
38. count and say

Difficulty: easy

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which
is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of groups
so that each group is a contiguous section all of the same character. Then for each group,
say the number of characters, then say the character. To convert the saying into a digit
string, replace the counts with a number and concatenate every saying.

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            nm1 = self.countAndSay(n-1)
            last = nm1[0]
            w = ""
            i = 0
            while i < len(nm1):
                c = 0
                while i < len(nm1) and nm1[i] == last:
                    i+=1
                    c+=1
                w = w+f"{c}{last}"
                last = nm1[i] if i < len(nm1) else None
            return w


if __name__ == "__main__":
    s = Solution()
    assert s.countAndSay(1) == "1"
    assert s.countAndSay(2) == "11"
    assert s.countAndSay(3) == "21"
    assert s.countAndSay(4) == "1211"
    assert s.countAndSay(5) == "111221"
    assert s.countAndSay(6) == "312211"