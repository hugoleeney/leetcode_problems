"""
143. Reorder List
Difficulty: Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
from utils import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        end = head
        while end.next:
            end.next.prev = end
            end = end.next

        while end is not head and head.next is not end:
            next_head = head.next

            head.next = end

            end.next = next_head

            end.prev.next = None

            end = end.prev

            head = next_head


if __name__ == "__main__":
    s = Solution()
    a = list_to_linked_list([1,2,3,4])
    s.reorderList(a)
    r = linked_list_to_list(a)
    assert r == [1,4,2,3], r
