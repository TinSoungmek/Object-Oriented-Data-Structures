class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, item):
        new_node = Node(item)
        self.size += 1
        if self.head == None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        print("Process")
        for i in range(self.size - 1):
            prev = None
            current = self.head
            for j in range(self.size - 1 - i):
                next_node = current.next

                if next_node is None:
                    break

                if prev is None:
                    current.next = next_node.next
                    next_node.next = current
                    self.head = next_node
                    prev = self.head
                else:
                    current.next = next_node.next
                    next_node.next = current
                    prev.next = next_node
                    prev = next_node

                print(self)

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)

L = LinkedList()
inp = input("input : ").split()
for i in inp:
    L.append(i)

print("Original")
print(L,"\n")
L.reverse()
print("\nReverse")
print(L)