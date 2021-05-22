# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        if head is None:
            return False

        nodeMap = {}
        while head.next is not None:
            if head in nodeMap.values():
                return True

            nodeMap[head.val] = head

            head = head.next

        return False


class Solution:
    def hasCycle(self, head):
        if head is None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast is None:
                return False
            if fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True