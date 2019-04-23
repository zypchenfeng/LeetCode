# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        #solution 2
        if not head:
            return None
        l_h = ListNode(-1)
        l = l_h
        r_h = ListNode(-1)
        r = r_h
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next
        l.next = r_h.next
        r.next = None
        return l_h.next

        # solution 1
        # if not head:
        #     return None
        # dummy = ListNode(0)
        # new_list = ListNode(0)
        # dummy.next = head
        # pre = dummy
        # cur = new_list
        # while head:
        #     if head.val < x:
        #         pre = pre.next
        #         head = head.next
        #     else:
        #         # cur.next, head, pre.next, cur = head, head.next, head, cur.next
        #         temp = head
        #         head = head.next
        #         pre.next = head
        #         temp.next = None
        #         cur.next = temp
        #         cur = cur.next
        #
        # pre.next = new_list.next
        # return dummy.next


a = [1, 4, 3, 2, 5, 2]
a.reverse()
head = ListNode(a[0])
for h in a[1:]:
    l = ListNode(h)
    l.next = head
    head = l

sol = Solution()
res = sol.partition(head, 3)
while res:
    print(res.val)
    res = res.next