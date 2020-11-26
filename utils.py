
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


def arr_assign(arr, key, val):
    try:
        arr[key] = val
        return
    except IndexError:
        # Do not extend the array for negative indices
        # That is ridiculously counterintuitive
        assert key >= 0
        arr.extend(((key + 1) - len(arr)) * [None])
        arr[key] = val
        return


def binary_tree_to_list(node):
    stack = [(node, 0)]
    result = []
    while stack:
        n, pos = stack.pop()
        arr_assign(result, pos, n.val)
        if n.left:
            stack.append((n.left, pos*2 +1))
        if n.right:
            stack.append((n.right, pos*2 +2))
    return result


if __name__ == "__main__":
    tc = [1,2,3,4,5,6,7]
    bt = list_to_binary_tree(tc)
    res = binary_tree_to_list(bt)
    assert tc == res


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(l):
    head = ListNode(l[0])
    cur = head
    for n in l[1:]:
        cur.next = ListNode(n)
        cur = cur.next
    return head


def linked_list_to_list(head):
    r = [head.val]
    while head.next:
        r.append(head.next.val)
        head = head.next
    return r