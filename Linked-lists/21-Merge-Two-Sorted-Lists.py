class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(head1: ListNode, head2: ListNode):
    dummy = ListNode(0)
    tail = dummy

    while head1 and head2:

        if head1.val < head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    tail.next = head1 or head2

    return dummy.next
