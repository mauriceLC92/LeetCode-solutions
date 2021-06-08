from typing import Counter


class LinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


my_node_1 = Node(5)
my_node_2 = Node(6)
my_node_3 = Node(7)

my_node_1.next = my_node_2
my_node_2.next = my_node_3

# 5 -> 6 -> 7 -> null


def log_node_values(head):
    if head is None:
        return "Nothing to log"
    while head is not None:
        print(head.val)

        head = head.next


def countNodes(head):
    counter = 0
    if head is None:
        return counter

    while head is not None:
        counter += 1

        head = head.next

    return counter


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


def detect_cyle_two_pointer(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next
    return True


def reverse_linked_list(head):

    current_node = head
    previous_node = None

    while current_node is not None:
        next_node_temp = current_node.next

        current_node.next = previous_node
        previous_node = current_node

        current_node = next_node_temp

    return previous_node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_list(l1: ListNode, l2: ListNode):

    dummy = ListNode(-100)
    tail = dummy

    curr_one = l1
    curr_two = l2

    while curr_one and curr_two:
        if curr_one.val < curr_two.val:
            tail.next = curr_one
            curr_one = curr_one.next
        else:
            tail.next = curr_two
            curr_two = curr_two.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy.next
