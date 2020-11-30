"""
199. Binary Tree Right Side View
Difficulty: medium


Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
from collections import deque
from typing import List

from utils import TreeNode, list_to_binary_tree


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque([(root, 0)])
        levels_leaders = {}
        while q:
            node, level = q.popleft()
            levels_leaders[level] = node

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return [v.val for k, v in sorted([(k, v) for k, v in levels_leaders.items()], key=lambda x: x[0])]


if __name__ == "__main__":
    Input = [1, 2, 3, None, 5, None, 4]
    Output = [1, 3, 4]

    s = Solution()
    assert s.rightSideView(list_to_binary_tree(Input)) == Output