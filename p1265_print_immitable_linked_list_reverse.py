"""
1265, print immutable linked list reverse
Difficulty: medium


You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):

ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.
The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.



Example 1:

Input: head = [1,2,3,4]
Output: [4,3,2,1]
"""


# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
class ImmutableListNode:
    def __init__(self, registry, val=None, next=None):
        self.registry = registry
        self.val = val
        self.next = next

    def printValue(self) -> None: # print the value of this node.
        self.registry.print(self.val)

    def getNext(self) -> 'ImmutableListNode': # return the next node.
        return self.next



class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head.getNext() is None:
            head.printValue()
        else:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()


class Registry():

    def __init__(self):
        self.print_order = []

    def print(self, val):
        self.print_order.append(val)


def list_to_linked_list(a, registry):
    head = ImmutableListNode(registry, a[0])
    curr = head
    for i in a[1:]:
        curr.next = ImmutableListNode(registry, i)
        curr = curr.next
    return head


if __name__ == "__main__":
    s = Solution()
    reg = Registry()
    a = [1,2,3,4,5,6]
    head = list_to_linked_list(a, reg)
    s.printLinkedListInReverse(head)
    assert reg.print_order == [6,5,4,3,2,1]

