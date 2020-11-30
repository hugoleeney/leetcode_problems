"""
111. Minimum Depth of Binary Tree
Easy

Giv
en a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2


Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""
from collections import deque
from utils import TreeNode, list_to_binary_tree


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = deque([(root, 1)])
        while d:
            node, depth = d.pop()

            leaf = True
            if node.left:
                d.appendleft((node.left, depth + 1))
                leaf = False
            if node.right:
                d.appendleft((node.right, depth + 1))
                leaf = False
            if leaf:
                return depth


if __name__ == "__main__":
    s = Solution()
    root = list_to_binary_tree([3,9,20,None,None,15,7])
    assert s.minDepth(root) == 2