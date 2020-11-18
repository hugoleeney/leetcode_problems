"""
2. Add Two Numbers

Difficulty: Medium

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single
digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

"""

"""
Comment: Not a particularly fast way of doing it. Could improve by doing a sum in decimal.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __cmp__(self, other):
        return self.val == other.val and self.next == other.next
    def __eq__(self, other):
        return self.val == other.val and self.next == other.next if other else False
    def __str__(self):
        node = self
        b = [self.val]
        while node.next:
            node = node.next
            b.append(node.val)
        return str(b)
    def __repr__(self):
        return self.__str__()


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode()
        node = result
        while l1 or l2 or carry:
            node.next = ListNode()
            node = node.next
            v = carry
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next
            node.val = v if v < 10 else v-10
            carry = 1 if v > 9 else 0
        return result.next



def ListNodesFromList(l):
    r = ListNode(l[-1], None)
    for i in reversed(l[:-1]):
        r = ListNode(i, r)
    return r

if __name__ == "__main__":

    # test ListNodesFromList
    assert ListNodesFromList([1]) == ListNode(1, None)
    assert ListNodesFromList([1,2]) == ListNode(1, ListNode(2, None))

    s = Solution()
    r = s.addTwoNumbers(ListNodesFromList([2,4,3]), ListNodesFromList([5,6,4]))
    assert r == ListNodesFromList([7,0,8])