'''
820. Short Encoding of Words

Difficulty - medium

Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
 

Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.

'''


class Solution:

    def register_count(self, c):
        self.count_n += c

    def minimumLengthEncoding(self, words: List[str]) -> int:
        self.count_n = 0
        root = {}
        for w in words:
            curr = root
            for l in w[::-1]:
                curr = curr.setdefault(l, {})
        word_dft(root, self.register_count)
        return self.count_n


def word_dft(n, f):
    for n, children in n.items():
        dft(children, 1, f)


def dft(n, depth, f):
    if n:
        for l, children in n.items():
            dft(children, depth + 1, f)
    else:
        f(depth + 1)

