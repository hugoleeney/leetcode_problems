"""
1119. Remove Vowels from a String
Easy


Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.



Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"


Example 2:

Input: "aeiou"
Output: ""


Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
"""


vowels = set(['a', 'e', 'i', 'o', 'u'])


class Solution:
    """
    could also assemble a list of characters and join at the end ...
    """
    def removeVowels(self, S: str) -> str:
        returned = ""
        for ch in S:
            if ch not in vowels:
                returned += ch
        return returned


if __name__ == "__main__":
    s = Solution()
    assert s.removeVowels("leetcodeisacommunityforcoders") == "ltcdscmmntyfrcdrs"