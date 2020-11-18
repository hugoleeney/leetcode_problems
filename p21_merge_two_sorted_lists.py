"""
21. Merge Two Sorted Lists

Difficulty: Easy

Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the
first two lists.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode()
        curr = r
        while True:
            if l1:
                if l2 and l2.val < l1.val:
                    curr.next = l2
                    curr = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    curr = l1
                    l1 = l1.next
            elif l2:
                curr.next = l2
                curr = l2
                l2 = l2.next
            else:
                break
        return r.next
