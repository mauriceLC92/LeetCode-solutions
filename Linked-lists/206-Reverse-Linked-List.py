# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


my_node_1 = Node(5)
my_node_2 = Node(6)
my_node_3 = Node(7)

my_node_1.next = my_node_2
my_node_2.next = my_node_3


def get_linked_list_values(head: ListNode):
    linked_list_values = ""
    while head is not None:
        linked_list_values += str(head.val)
        head = head.next

    return linked_list_values


# This solution seems to work but returns an empty list on LeetCode
def reverseList(head: ListNode) -> ListNode:
    if head is None:
        return head

    values = get_linked_list_values(head)
    max_values_index = len(values) - 1

    while max_values_index >= 0:
        head.val = int(values[max_values_index])
        head = head.next
        max_values_index -= 1
    return head


reverseList(my_node_1)
print("my_node_1.val", my_node_1.val)
print("my_node_2.val", my_node_2.val)
print("my_node_3.val", my_node_3.val)
print("my_node_3.next", my_node_3.next)


def reverseListOptimal(head: ListNode) -> ListNode:
    current_node = head
    previous_node = None

    while current_node is not None:
        next_node_temp = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node_temp

    return previous_node
