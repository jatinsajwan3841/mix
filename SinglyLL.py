class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LL:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)

    def pushFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pushAfter(self, key, data):
        if self.head == None:
            print("empty ll")
            return
        node = self.head
        while node:
            if node.data == key:
                newNode = Node(data)
                newNode.next = node.next
                node.next = newNode
                return
            node = node.next
        print("Element not found")

    def pop(self, key):
        if self.head == None:
            print("Empty LL")
            return
        node = self.head
        if node.data == key:
            self.head = node.next
            del node
            return
        prev = node
        node = prev.next
        while node is not None:
            if node.data == key:
                prev.next = node.next
                del node
                return
            prev = node
            node = node.next
        print("Key not found")

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return "->".join(nodes)


l1 = LL()
print(l1)
l1.push(1)
print(l1)
l1.push(2)
print(l1)
l1.pushFront(3)
print(l1)
l1.pushAfter(2, 5)
print(l1)
l1.pop(2)
print(l1)
