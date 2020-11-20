"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.



Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


Note:

1 <= X <= customers.length == grumpy.length <= 20000
0 <= customers[i] <= 1000
0 <= grumpy[i] <= 1
"""
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        max_cheat = sum((x for idx, x in enumerate(customers[0:X]) if grumpy[idx] == 1))
        cheat = max_cheat
        max_cheat_idx = 0
        for idx, c in enumerate(customers[1:len(customers) - X + 1]):
            prior_cheat = cheat
            cheat = cheat - (customers[idx] if grumpy[idx] else 0) + (customers[idx + X] if grumpy[idx + X] else 0)
            if cheat > max_cheat:
                max_cheat = cheat
                max_cheat_idx = idx + 1
        satisfied = max_cheat + sum((x for idx, x in enumerate(customers) if grumpy[idx] == 0))
        return satisfied


if __name__ == "__main__":
    s = Solution()
    assert s.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3)