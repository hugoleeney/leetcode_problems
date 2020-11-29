"""
1375. Bulb Switcher III
Medium

There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.



Example 1:



Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.


Example 2:

Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).


Constraints:

n == light.length
1 <= n <= 5 * 10^4
light is a permutation of  [1, 2, ..., n]
"""


from typing import List


class SolutionSlow:
    def numTimesAllBlue(self, light: List[int]) -> int:
        states = [0] * len(light)
        all_up_to = -1
        max = 0
        returned = 0
        for i in range(len(light)):
            l_num = light[i] - 1
            states[l_num] = 1
            while all_up_to+1 < len(states) and states[all_up_to+1]:
                all_up_to += 1
            if l_num > max:
                max = l_num
            if max == all_up_to:
                returned += 1
        return returned



class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        sum = 0
        result = 0
        for i in range(1, len(light) + 1):
            sum += light[i - 1]
            if sum == (i * (i + 1)) // 2:
                result += 1
        return result


if __name__ == "__main__":
    tc = [2,1,3,5,4]
    s = Solution()
    assert s.numTimesAllBlue(tc) == 3