# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast and fast.next:
            if fast.val == fast.next.val:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                fast = fast.next
                slow.next = fast
            else:
                slow = slow.next
                fast = fast.next
        return dummy.next


a = [1, 1, 1, 2, 3]
a.reverse()
head = ListNode(a[0])
for h in a[1:]:
    l = ListNode(h)
    l.next = head
    head = l
print('Head is')
temp = head
while temp:
    print(temp.val)
    temp = temp.next

print('Solution is')
sol = Solution()
res = sol.deleteDuplicates(head)
while res:
    print(res.val)
    res = res.next

a = [1, 2, 2, 3, 4, 5, 5]
a.reverse()
head = ListNode(a[0])
for h in a[1:]:
    l = ListNode(h)
    l.next = head
    head = l
print('Head is')
temp = head
while temp:
    print(temp.val)
    temp = temp.next

print('Solution is')
sol = Solution()
res = sol.deleteDuplicates(head)
while res:
    print(res.val)
    res = res.next