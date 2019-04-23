class ListNode(self, val = None):
    self.val = val
    self.next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        countA = 0
        countB = 0
        a = headA
        b = headB
        while headA.next:
            countA += 1
            a = a.next
        while headB.next:
            countB += 1
            b = b.next
        if countA >= countB:
            for i in range(countA-countB):
                headA = headA.next
        else:
            for i in range(countB - countA):
                headB = headB.next
        while headA.next:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None

        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa

sol = Solution()



