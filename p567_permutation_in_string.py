"""
567. Permutation in string
Difficulty: medium

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
import math
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1 = sorted(s1)
        for j in range(len(s1), len(s2) + 1):
            i = j - len(s1)
            if sorted(s2[i:j]) == s1:
                return True
        return False



class Solution1:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        ref = Counter(s1)
        to_match = len(ref)
        c = Counter(s2[0:len(s1)])
        matching = set([letter for letter in c.keys() if c[letter] == ref[letter]])
        if len(matching) == to_match:
            return True

        for j in range(len(s1), len(s2)):
            i = j - len(s1)

            ch_at_j = s2[j]
            c[ch_at_j] += 1

            if ref[ch_at_j] != 0 and ref[ch_at_j] == c[ch_at_j]:
                matching.add(ch_at_j)
            else:
                matching.discard(ch_at_j)

            ch_at_i = s2[i]
            c[ch_at_i] -= 1
            if ref[ch_at_i] != 0 and ref[ch_at_i] == c[ch_at_i]:
                matching.add(ch_at_i)
            else:
                matching.discard(ch_at_i)

            if len(matching) == to_match:
                return True

        return False


def primes(num):
    prev = 2
    yield prev
    sofar = [prev]
    n = 1
    while n < num:
        prev += 1
        for i in sofar:
            if i > math.sqrt(prev):
                n += 1
                sofar.append(prev)
                yield prev
                break
            if prev % i == 0:
                break


primes = [p for p in primes(26)]


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_code = math.prod([primes[ord(ch) - 97] for ch in s1])
        s2_code = math.prod([primes[ord(ch) - 97] for ch in s2[0:len(s1)]])
        if s1_code == s2_code:
            return True
        for j in range(len(s1), len(s2)):
            i = j - len(s1)
            s2_code = (s2_code * primes[ord(s2[j]) - 97]) // primes[ord(s2[i]) - 97]
            if s2_code == s1_code:
                return True
        return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    s = Solution()
    assert s.checkInclusion(s1, s2)
    assert not s.checkInclusion(s1, "eidbooo")


    s = Solution2()
    assert s.checkInclusion(s1, s2)
    assert not s.checkInclusion(s1, "eidbooo")
