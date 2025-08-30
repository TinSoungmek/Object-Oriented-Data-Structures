class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
        
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0
    
    def append(self,data):
        new_node = self.Node(data)
        self.size += 1
        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current and current.next:
                next_node = current.next

                if current.value > next_node.value:
                    print(f"\nSwapping {current.value} and {next_node.value}")
                    current.value, next_node.value = next_node.value, current.value
                    swapped = True
                    print(f"List: {self}")
                current = current.next
    
    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node.value))
            node = node.next
        return '->'.join(ans)
    
L = LinkedList()
print("*****Bubble Sort Linked List*****")
inp = input("Enter Input: ").split(",")
for i in inp:
    L.append(int(i))
print(f"Input List: {L}")
print("_______________________________________")
L.bubble_sort()
print("_______________________________________")
print(f"Sorted List: {L}")