from functools import lru_cache
from typing import List

from p1406_test_case import tc1
class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.stoneValue = stoneValue
        best = self.do(0)
        if best > 0:
            return "Alice"
        elif best < 0:
            return "Bob"
        else:
            return "Tie"

    def length(self, i):
        return len(self.stoneValue) - i

    @lru_cache()
    def do(self, i) -> int:
        length = len(self.stoneValue) - i
        if length > 4:
            return max(
                self.stoneValue[i] - self.do(i+1),
                sum(self.stoneValue[i:i+2]) - self.do(i+2),
                sum(self.stoneValue[i:i+3]) - self.do(i+3)
            )
        elif length == 4:
            return max(
                self.stoneValue[i] - self.do(i+1),
                sum(self.stoneValue[i:i+2]) - self.do(i+2),
                sum(self.stoneValue[i:i+3]) - self.stoneValue[i+3]
            )
        elif length == 3:
            return max(
                self.stoneValue[i] - self.do(i+1),
                sum(self.stoneValue[i:i+2]) - self.stoneValue[i+2],
                sum(self.stoneValue[i:i+3])
            )
        elif length == 2:
            return max(
                self.stoneValue[i] - self.stoneValue[i+1],
                sum(self.stoneValue[i:i+2])
            )
        elif length == 1:
            return self.stoneValue[i]
        elif length == 0:
            return 0


    # negative value
    # def stoneGameIII(self, stoneValue: List[int]) -> str:
    #     if len()
    #     max_score = 0
    #     max_idx = 0
    #     for i in range(1,min(len(stoneValue), 4)):
    #         score = sum(stoneValue[0:i])
    #         if score > max_score:
    #             max_score = score
    #             max_idx = i
    #     return max_score - sum(stoneValue[max_idx:])


if __name__ == "__main__":
    import time
    start = time.perf_counter()
    s = Solution()
    a = [8,-3,7,8,-1,1,-16,-12,-13,5,17,-7,-12,8,12,-12,16,13,4,6,-2,-14,2]
    a = [-3,4,-7,7,-8,-4,-12,-8,11,-11,-3,-1,13,14,0,9,-13,-17,-6,10,15,-1,7]
    assert s.stoneGameIII(a) == "Tie"
    print(time.perf_counter() - start)


class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        best = self.do(",".join([str(x) for x in stoneValue]))
        if best > 0:
            return "Alice"
        elif best < 0:
            return "Bob"
        else:
            return "Tie"

    @lru_cache()
    def do(self, stoneValue) -> int:
        stoneValue = [int(x) for x in stoneValue.split(",")]
        if len(stoneValue) == 0:
            return 0
        if len(stoneValue) == 1:
            return stoneValue[0]
        if len(stoneValue) == 2:
            return max(
                stoneValue[0] - stoneValue[1],
                sum(stoneValue)
            )
        if len(stoneValue) == 3:
            return max(
                stoneValue[0] - self.do(",".join((str(x) for x in stoneValue[1:]))),
                sum(stoneValue[:2]) - stoneValue[2],
                sum(stoneValue)
            )
        if len(stoneValue) == 4:
            return max(
                stoneValue[0] - self.do(",".join((str(x) for x in stoneValue[1:]))),
                sum(stoneValue[:2]) - self.do(",".join((str(x) for x in stoneValue[2:]))),
                sum(stoneValue[:3]) - stoneValue[3]
            )
        return max(
            stoneValue[0] - self.do(",".join((str(x) for x in stoneValue[1:]))),
            sum(stoneValue[:2]) - self.do(",".join((str(x) for x in stoneValue[2:]))),
            sum(stoneValue[:3]) - self.do(",".join((str(x) for x in stoneValue[3:])))
        )

