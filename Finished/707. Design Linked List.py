class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            return self.head.val
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.addAtHead(val)
        elif self.size == 1:
            self.head.next = ListNode(val)
        else:
            cur = self.head
            for i in range(self.size-1):
                cur = cur.next
            cur.next = ListNode(val)
        self.size += 1


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of
        linked list, the node will be appended to the end of linked list. If index is greater than the length,
        the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif 0 < index < self.size:
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            node = ListNode(val)
            node.next = cur.next
            cur.next = node
            self.size += 1
        else:
            pass

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self.size >= 1:
            if index == 0:
                self.head = self.head.next
                self.size -= 1
            elif 0 < index < self.size:
                cur = self.head
                for i in range(index-1):
                    cur = cur.next
                cur.next = cur.next.next
                self.size -= 1
            else:
                pass






# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(7)
obj.addAtTail(7)
obj.addAtHead(9)
obj.addAtTail(8)
obj.addAtHead(6)
obj.addAtHead(0)
obj.get(5)
obj.addAtHead(0)
obj.get(2)
obj.get(5)
obj.addAtTail(4)
# obj.addAtIndex(1, 2)
# print(obj.get(1))
# obj.deleteAtIndex(1)
# print(obj.get(1))
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)
