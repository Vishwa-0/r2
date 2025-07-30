class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.next = None
        new_node.prev = current.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.tail = None
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                current.next.next.prev = current.next
                return
            current = current.next
            

    def display(self):
        current = self.head
        while current:
            print(current.data, end = "<->")
            current = current.next
        print("None")

linked = DoublyLinkedList()
linked.append(1)
linked.append(2)
linked.append(3)
print("Doubly linked List:")
linked.display()
linked.prepend(0)
linked.prepend(-1)
print("Doubly linked List after prepending values:")
linked.display()
linked.delete(2)
print("Doubly linked List after deleting values:")
linked.display()
