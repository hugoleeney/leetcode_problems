"""
1315. Sum of Nodes with Even-Valued Grandparent
Difficulty: medium

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.



Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
"""
from utils import TreeNode


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = [(root, 0)]
        d = {}
        sumy = 0
        while q:
            n, depth = q.pop()
            d[depth] = n.val
            if depth >= 2 and d[depth - 2] % 2 == 0:
                sumy += n.val
            if n.right:
                q.append((n.right, depth + 1))
            if n.left:
                q.append((n.left, depth + 1))
        return sumy


def list_to_binary_tree(a):
    root = TreeNode(a[0])
    q = [(root, 0)]
    while q:
        n, idx = q.pop()
        left_idx = idx*2 + 1
        right_idx = idx*2 + 2

        if right_idx < len(a) and a[right_idx]:
            n.right = TreeNode(a[right_idx])
            q.append((n.right, right_idx))
        if left_idx < len(a) and a[left_idx]:
            n.left = TreeNode(a[left_idx])
            q.append((n.left, left_idx))
    return root


if __name__ == "__main__":
    s = Solution()
    a = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
    root = list_to_binary_tree(a)
    assert s.sumEvenGrandparent(root) == 18, s.sumEvenGrandparent(root)