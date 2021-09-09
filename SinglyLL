class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end='=>')
            temp = temp.next

    def insertBeg(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def insertEnd(self, newData):
        newNode = Node(newData)
        if self.head == None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def remove(self, key):
        temp = self.head
        if temp == None:
            print('empty LL')
            return
        if temp.data == key:
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

LL = LinkedList()
LL.head = Node(1)
second = Node(2)
third = Node(3)
LL.head.next = second
second.next = third

LL.traverse()
LL.insertBeg(int(input()))
LL.insertEnd(int(input()))
LL.remove(int(input()))
LL.traverse()
