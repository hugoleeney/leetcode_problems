"""
958.
Difficulty: Medium

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = deque([(root, 0)])
        incomplete_level = None
        while q:
            node, depth = q.pop()

            if node.left:
                if incomplete_level and incomplete_level <= depth + 1:
                    return False
                q.appendleft((node.left, depth + 1))
            else:
                incomplete_level = depth + 1

            if node.right:
                if incomplete_level and incomplete_level == depth + 1:
                    return False
                q.appendleft((node.right, depth + 1))
            else:
                incomplete_level = depth + 1

        return True


if __name__ == "__main__":
    s = Solution()
    from utils import list_to_binary_tree
    tree = list_to_binary_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,None,None,15])
    s.isCompleteTree(tree)