"""
654. Maximum Binary Tree
Difficulty: Medium

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        index_of_max = nums.index(max(nums))
        left = self.constructMaximumBinaryTree(nums[0: index_of_max])
        right = self.constructMaximumBinaryTree(nums[index_of_max + 1:])

        return TreeNode(nums[index_of_max], left, right)


if __name__ == "__main__":
    s = Solution()
    r = s.constructMaximumBinaryTree([3,2,1,6,0,5])
    assert r == TreeNode(6, TreeNode(3, None, TreeNode(2, None, TreeNode(1))), TreeNode(5, TreeNode(0)))