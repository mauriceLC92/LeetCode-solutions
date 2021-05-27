class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

    a_set = set()

    while headA is not None:
        a_set.add(headA)
        headA = headA.next

    while headB is not None:
        if headB in a_set:
            return headB
        headB = headB.next

    return None
