"""
1302. Deepest Leaves Sum
Difficulty: medium

Given a binary tree, return the sum of values of its deepest leaves.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [(root,0)]
        deepest = 0
        sumy = 0
        while q:
            n, depth = q.pop()
            if n.left == None and n.right == None:
                if depth > deepest:
                    sumy = n.val
                    deepest = depth
                elif depth == deepest:
                    sumy += n.val
            else:
                if n.right:
                    q.append((n.right, depth+1))
                if n.left:
                    q.append((n.left, depth+1))
        return sumy
