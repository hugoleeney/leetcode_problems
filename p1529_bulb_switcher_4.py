"""
1529. Bulb Switcher 4
Medium


There is a room with n bulbs, numbered from 0 to n-1, arranged in a row from left to right. Initially all the bulbs are turned off.

Your task is to obtain the configuration represented by target where target[i] is '1' if the i-th bulb is turned on and is '0' if it is turned off.

You have a switch to flip the state of the bulb, a flip operation is defined as follows:

Choose any bulb (index i) of your current configuration.
Flip each bulb from index i to n-1.
When any bulb is flipped it means that if it is 0 it changes to 1 and if it is 1 it changes to 0.

Return the minimum number of flips required to form target.



Example 1:

Input: target = "10111"
Output: 3
Explanation: Initial configuration "00000".
flip from the third bulb:  "00000" -> "00111"
flip from the first bulb:  "00111" -> "11000"
flip from the second bulb:  "11000" -> "10111"
We need at least 3 flip operations to form target.


Example 2:

Input: target = "101"
Output: 3
Explanation: "000" -> "111" -> "100" -> "101".
"""


class Solution:
    def minFlipsSlow(self, target: str, last='0') -> int:

        if len(target) == 0:
            return 0
        else:
            if target[0] == last:
                return self.minFlips(target[1:], last)
            else:
                return 1 + self.minFlips(target[1:], '1' if last == "0" else '0')

    def minFlips(self, target: str) -> int:
        curr = '0'
        result = 0
        for i in target:
            if i != curr:
                result += 1
                curr = '1' if curr == "0" else '0'
        return result


if __name__ == "__main__":
    s = Solution()
    assert s.minFlips("10111") == 3
