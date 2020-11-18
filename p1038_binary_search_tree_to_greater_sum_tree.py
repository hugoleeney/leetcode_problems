"""
1038. Binary Search Tree to Greater Sum Tree
Difficulty: Medium

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return other is not None and self.val == other.val and self.left == other.left and self.right == other.right


class Solution:
    def bstToGst(self, root: TreeNode, parent_val=0) -> TreeNode:
        root.tot = root.val
        if root.right != None:
            right = self.bstToGst(root.right, parent_val)
            root.val += right.tot
            root.tot += right.tot
        root.val += parent_val
        if root.left != None:
            root.tot += self.bstToGst(root.left, root.val).tot
        return root


def list_to_binary_tree(a):
    root = TreeNode(a[0])
    q = [(root, 0)]
    while q:
        n, idx = q.pop()
        left_idx = idx*2 + 1
        right_idx = idx*2 + 2

        if right_idx < len(a) and a[right_idx] is not None:
            n.right = TreeNode(a[right_idx])
            q.append((n.right, right_idx))
        if left_idx < len(a) and a[left_idx] is not None:
            n.left = TreeNode(a[left_idx])
            q.append((n.left, left_idx))
    return root


if __name__ == "__main__":
    a = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    bt = list_to_binary_tree(a)
    expected = [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
    bt_expected = list_to_binary_tree(expected)
    s = Solution()
    result = s.bstToGst(bt)
    assert result == bt_expected