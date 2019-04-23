# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Solution 1
        # if not head:
        #     return None
        # dummy = ListNode(0)
        # dummy.next = head
        # pre = dummy
        #
        # for i in range(m-1):
        #     pre = pre.next
        # reverse = None
        # cur = pre.next
        # for i in range(n-m+1):
        #     cur.next, reverse, cur = reverse, cur, cur.next
        # pre.next.next = cur
        # pre.next = reverse
        # return dummy.next

        # solution 2
        if m==n:
            return head
        m_node = None
        
        counter = 0

        # node_before = None
        # new_n_node = None
        # prev = None
        # count = 0
        # current = head
        #
        # while current and count < n:
        #     count += 1
        #     next_node = current.next
        #
        #     if count + 1 == m:
        #         node_before = current
        #     if count == m:
        #         new_n_node = current
        #
        #     if m <= count <= n:
        #         current.next = prev
        #         prev = current
        #
        #     current = next_node
        #
        # new_n_node.next = current
        # if node_before is not None:
        #     node_before.next = prev
        #
        # if m == 1:
        #     head = prev
        #
        # return head





a = [1, 2, 3, 4, 5]
a.reverse()
head = ListNode(a[0])
for h in a[1:]:
    l = ListNode(h)
    l.next = head
    head = l

sol = Solution()
res = sol.reverseBetween(head, 2, 4)
while res:
    print(res.val)
    res = res.next
#
#
# a = [1, 2]
# a.reverse()
# head = ListNode(a[0])
# for h in a[1:]:
#     l = ListNode(h)
#     l.next = head
#     head = l
# print('Head is')
# temp = head
# while temp:
#     print(temp.val)
#     temp = temp.next
#
# print('Solution is')
# sol = Solution()
# res = sol.rotateRight(head, 1)
# while res:
#     print(res.val)
#     res = res.next
#
# a = [1]
# a.reverse()
# head = ListNode(a[0])
# for h in a[1:]:
#     l = ListNode(h)
#     l.next = head
#     head = l
# print('Head is')
# temp = head
# while temp:
#     print(temp.val)
#     temp = temp.next
#
# print('Solution is')
# sol = Solution()
# res = sol.rotateRight(head, 1)
# while res:
#     print(res.val)
#     res = res.next