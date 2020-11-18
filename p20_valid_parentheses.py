"""
20. Valid Parentheses

Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

from collections import deque


d = {
    '[': "]",
    '{': "}",
    '(': ")"
}


dr = {
    ']': "[",
    '}': "{",
    ')': "("
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in d:
                stack.append(c)
            else:
                try:
                    if stack.pop() != dr[c]:
                        return False
                except IndexError as e:
                    return False
        return False if stack else True


if __name__ == "__main__":
    s = Solution()
    p = "{[]}"
    assert s.isValid(p) == True
