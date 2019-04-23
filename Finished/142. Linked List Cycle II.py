# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        if (fast is None) or (fast.next is None) or (fast.next.next is None):
            return None
        slow = slow.next
        fast = fast.next.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if fast is None:
                return None
        A = head
        while A != slow:
            A = A.next
            slow = slow.next
        return A