"""
987. Vertical Order Traversal of a Binary Tree
Difficulty: medium

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.



Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
"""
from collections import deque
from typing import List


# Definition for a binary tree node.
from utils import list_to_binary_tree, TreeNode


class Solution:
    """
    potentially better solution would be to use a list for `columns`. However,
    Leetcode's test case run times do not benefit from such a change.
    """

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        columns = {}

        q = deque([(root, 0, 0)])
        while q:
            node, col, level = q.popleft()

            relevant_col = columns.setdefault(col, [])
            # if relevant_col and level == relevant_col[-1][0] and relevant_col[-1][1] > node.val:
            #     t = relevant_col.pop()
            #     relevant_col.append((level, node.val))
            #     relevant_col.append(t)
            # else:
            relevant_col.append((level, node.val))

            if node.left:
                q.append((node.left, col - 1, level + 1))
            if node.right:
                q.append((node.right, col + 1, level + 1))

        return [[x[1] for x in sorted(v)] for k, v in sorted([(k, v) for k, v in columns.items()], key=lambda x: x[0])]



if __name__ == "__main__":
    s = Solution()
    tc = [3,9,20,None,None,15,7]
    tc = list_to_binary_tree(tc)
    expected = [[9],[3,15],[20],[7]]
    assert s.verticalTraversal(tc) == expected