from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# l1 = [2,4,3], l2 = [5,6,4]


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    current_one = l1
    current_two = l2

    carry_over = 0

    result = ListNode(0)
    result_tail = result

    while current_one or current_two or carry_over:
        val1 = current_one.val if current_one else 0
        val2 = current_two.val if current_two else 0

        carry_over, output = divmod(val1 + val2 + carry_over, 10)

        result_tail.next = ListNode(output)
        result_tail = result_tail.next

        current_one = current_one.next if current_one else None
        current_two = current_two.next if current_two else None

    return result.next


starting_node = ListNode(1)

current = starting_node

current.next = ListNode(5)