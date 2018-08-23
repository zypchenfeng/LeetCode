# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        new_list = slow.next
        new_list = self.reverse_list(new_list)
        slow.next = None
        while new_list:
            if new_list.val != head.val:
                return False
            new_list = new_list.next
            head = head.next
        return True

    def reverse_list(self, head):
        if not head:
            return None
        res = None
        while head:
            head.next, res, head = res, head, head.next
        return res

a = [0]
a.reverse()
head = ListNode(a[0])
for h in a[1:]:
    l = ListNode(h)
    l.next = head
    head = l

sol = Solution()
res = sol.isPalindrome(head)
print(res)
# while res:
#     print(res.val)
#     res = res.next