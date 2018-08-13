# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #  solution 1
        # if not head:
        #     return None
        # pa = head
        # pb = head
        # length = 1
        # while pa.next:
        #     length += 1
        #     pa = pa.next
        # pa.next = head  # form a circle
        # n = k%length
        # for i in range(length - n -1):
        #     pb = pb.next
        # res = pb.next
        # pb.next = None
        # return res

        # Solution 2
        if not head:
            return None

        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next

        k %= length

        fast = slow = head
        for i in range(k):
            fast = fast.next

        while fast.next:
            slow, fast = slow.next, fast.next

        fast.next = head           # fast reached the end of the linked list
        head = slow.next           # the beginning of the k-th from right
        slow.next = None           # cut the tail off

        return head


        # if not head:
        #     return head
        #
        # length = 0
        # cur = head
        # while cur:
        #     length += 1
        #     cur = cur.next
        #
        # k %= length
        # slow = fast = head
        # for i in range(k):
        #     fast = fast.next
        #
        # while fast.next:
        #     slow, fast = slow.next, fast.next
        #
        # fast.next = head
        # head = slow.next
        # slow.next = None
        # return head

a = [1, 2, 3, 4, 5]
a.reverse()
head = ListNode(a[0])
for h in a[1:]:
    l = ListNode(h)
    l.next = head
    head = l

sol = Solution()
res = sol.rotateRight(head, 2)
while res:
    print(res.val)
    res = res.next


a = [1, 2]
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
res = sol.rotateRight(head, 1)
while res:
    print(res.val)
    res = res.next
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