"""
1402. Reducing Dishes
Difficulty: hard

A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  time[i]*satisfaction[i]

Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.



Example 1:

Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total Like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.
"""
from functools import lru_cache
from typing import List


class DynamicProgrammingSolution:
    """
    This exceeds the time limit (does a lot of unnecessary work) but is an easy solution to write
    """

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        self.satisfaction = satisfaction
        return self.do(0, len(satisfaction))

    @lru_cache()
    def do(self, start, end, idx=1) -> int:
        length = end - start
        if length == 1:
            if self.satisfaction[start] > 0:
                return self.satisfaction[start + 0] * idx
            else:
                return 0
        else:
            return max(
                self.satisfaction[start] * idx + self.do(start + 1, end, idx + 1),
                self.do(start + 1, end, idx)
            )


class Solution:
    """
    This passes the tests but also does unnecessary work.
    Once you sort the satisfaction
    """
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        positives = []
        negatives = []
        for i in satisfaction:
            if i < 0:
                negatives.append(i)
            else:
                positives.append(i)
        positives.sort()

        sum_positive = sum(positives)

        result_positive = sum(((idx + 1) * i for idx, i in enumerate(positives)))

        negatives.sort()

        best = 0
        for idx, i in enumerate(negatives):
            sum_affects = 0
            for jdx in range(0, len(negatives) - idx):
                contribution = sum_positive + (negatives[idx + jdx] * (jdx + 1))
                sum_affects += contribution
            if sum_affects > best:
                best = sum_affects

        return result_positive + best


if __name__ == "__main__":
    s = Solution()
    assert s.maxSatisfaction([-1,-8,0,5,-9]) == 14
