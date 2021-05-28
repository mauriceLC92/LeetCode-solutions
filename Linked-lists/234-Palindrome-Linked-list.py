# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import deque


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        current = head
        previous = None
        my_stack = deque([])

        while current is not None:
            my_stack.append(current)

            next_node_temp = current.next
            current.next = previous
            previous = current
            current = next_node_temp

        is_palindrome = False
        while previous:
            if previous.val == my_stack.popleft().val:
                is_palindrome = True
            else:
                is_palindrome = False
                return is_palindrome
            previous = previous.next
        return is_palindrome