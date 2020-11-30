"""
938. Range Sum of BST
Easy

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].



Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
"""
from utils import TreeNode, list_to_binary_tree


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = [root]
        total = 0
        while stack:
            node = stack.pop()
            if node.val >= low and node.val <= high:
                total += node.val

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return total


if __name__ == "__main__":
    s = Solution()
    root = [10, 5, 15, 3, 7, None, 18]
    root = list_to_binary_tree(root)
    low = 7
    high = 15
    assert s.rangeSumBST(root, low, high) == 32