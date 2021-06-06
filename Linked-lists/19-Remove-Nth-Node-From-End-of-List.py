# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:

    dummy = ListNode(-1)
    dummy.next = head

    fast = dummy
    slow = dummy

    index = 0

    while index < n:
        index += 1
        fast = fast.next

    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    slow = slow.next.next

    return dummy.next
