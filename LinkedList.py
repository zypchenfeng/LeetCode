class Node:
    def __init__(self, data = None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = Node()
    def append(self, data):
        new_node=Node(data)
        # if self.head.val == None:
        #     self.head = new_node
        # else:
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
    def length(self):
        res = 0
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            res += 1            
        return res
    def display(self):
        elements =[]
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
            elements.append(cur_node.val)            
        print(elements)
    def get(self, index):
        if index > self.length() or index < 0:
            print('False index')
        else:
            counter = 0
            cur_node = self.head
            while cur_node.next and counter != index:
                cur_node = cur_node.next
                counter += 1 
            return cur_node.val

    def __getitem__(self,index):
        return self.get(index)
    def erase(self, index):
        if index >= self.length() or index < 0:
            print('False erasing index')
            return False
        else:
            pre_node = self.head
            cur_node = self.head.next
            counter = 0
            while cur_node.next and counter != index:
                pre_node = pre_node.next
                cur_node = cur_node.next
                counter += 1
            pre_node.next = cur_node.next              
    # def insert(self, index, data):
        
    # def insert_node(self, index, data):
    # def set(self,index,data):

if __name__ == "__main__":
    myList = LinkedList()
    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    myList.display()
    # print(myList.length())
    # print('Get index 3: ', myList.get(3))
    myList.erase(1)
    print('erase index 1: ')
    myList.display()




