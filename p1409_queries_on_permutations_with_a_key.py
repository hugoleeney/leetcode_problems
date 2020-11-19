"""
1409. Queries on a Permutation With Key
Difficulty: medium

Given the array queries of positive integers between 1 and m, you have to process all queries[i] (from i=0 to i=queries.length-1) according to the following rules:

In the beginning, you have the permutation P=[1,2,3,...,m].
For the current i, find the position of queries[i] in the permutation P (indexing from 0) and then move this at the beginning of the permutation P. Notice that the position of queries[i] in P is the result for queries[i].
Return an array containing the result for the given queries.



Example 1:

Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1]
Explanation: The queries are processed as follow:
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is 2, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5].
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5].
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is 2, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5].
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is 1, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5].
Therefore, the array containing the result is [2,1,2,1].


NOTES:
    leetcode submission test cases are too short to determine 'fastness' of an algorithm.
        Solution1 below performs badly on the website. Below it outperforms Solution2
"""
from typing import List


class Solution1:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        db_val_to_pos = {x: x - 1 for x in range(1, m + 1)}
        db_pos_to_val = {x - 1: x for x in range(1, m + 1)}

        result = []
        for query in queries:
            pos_of_query = db_val_to_pos[query]
            result.append(pos_of_query)

            for i in range(pos_of_query - 1, -1, -1):
                val = db_pos_to_val[i]
                db_pos_to_val[i + 1] = val
                db_val_to_pos[val] = i + 1

            db_pos_to_val[0] = query
            db_val_to_pos[query] = 0

        return result

class Solution2:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [x for x in range(1,m+1)]
        result = []
        for query in queries:
            result.append(arr.index(query))
            arr.insert(0,arr.pop(result[-1]))
        return result


if __name__ == "__main__":
    import time

    m = 100000
    queries = [50000]*100000
    start = time.perf_counter()
    s = Solution2()
    r1 = s.processQueries(queries, m)
    print(time.perf_counter() - start)


    start = time.perf_counter()
    s = Solution1()
    r2 = s.processQueries(queries, m)
    print(time.perf_counter() - start)

    assert r1 == r2
