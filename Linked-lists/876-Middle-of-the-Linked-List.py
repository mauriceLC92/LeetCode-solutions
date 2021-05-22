# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def count_nodes(head: ListNode):
    counter = 0

    while head is not None:
        counter += 1
        head = head.next
    return counter


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        amount_of_nodes = count_nodes(head)
        middle_node = (amount_of_nodes // 2) + 1

        counter = 0

        while head is not None:
            counter += 1
            if counter == middle_node:
                return head
            head = head.next
