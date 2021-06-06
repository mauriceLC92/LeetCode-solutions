# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# head = [1,2,3,4]
# swap one output -> [2,1,3,4]
# output -> [2,1,4,3]
def swapPairs(head: ListNode):

    dummy = ListNode(-1, head)
    previous = dummy

    current = head

    while current and current.next:
        first = current
        second = current.next
        next_pair = current.next.next

        second.next = first
        first.next = next_pair
        previous.next = second

        previous = first
        current = next_pair

    return dummy.next
