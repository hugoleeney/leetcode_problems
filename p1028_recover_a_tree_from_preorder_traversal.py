"""

"""
from utils import list_to_binary_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recoverFromPreorder(self, S: str) -> TreeNode:

        val = ""
        i = 0
        while i < len(S) and S[i] != "-":
            val += S[i]
            i += 1
        val = int(val)
        root = TreeNode(val)
        branches = [root]
        prev_depth = 0
        while i < len(S):
            next_depth = 0
            while S[i] == "-":
                next_depth += 1
                i += 1
            pops = next_depth - prev_depth if next_depth > prev_depth else abs(next_depth - prev_depth) + 2

            val = ""
            while i < len(S) and S[i] != "-":
                val += S[i]
                i += 1
            val = int(val)

            for _ in range(pops):
                parent = branches.pop()
            if not parent.left:
                parent.left = TreeNode(val)
                branches.append(parent)
                branches.append(parent.left)
            else:
                parent.right = TreeNode(val)
                branches.append(parent)
                branches.append(parent.right)
            prev_depth = next_depth
        return root


if __name__ == "__main__":
    s = Solution()
    expected = list_to_binary_tree([1,2,5,3,None,6,None,4,None,7])
    s.recoverFromPreorder("1-2--3---4-5--6---7") == expected

