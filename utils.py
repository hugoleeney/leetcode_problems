
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return other is not None and self.val == other.val and self.left == other.left and self.right == other.right



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