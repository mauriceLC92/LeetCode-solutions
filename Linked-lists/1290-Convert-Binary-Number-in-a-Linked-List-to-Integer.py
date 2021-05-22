# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head) -> int:
        if head is None:
            return 0

        binary_string = ""
        while head is not None:
            binary_string += head.val
            head = head.next

        return int(binary_string, 2)
