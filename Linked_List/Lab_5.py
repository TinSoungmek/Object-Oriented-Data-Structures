class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        s = ""
        current_node = self.head
        while current_node:
            s += current_node.value
            if current_node.next:
                s += " → "
            current_node = current_node.next
        return s

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def reverse_group(self, start, k):
        prev = None
        current = start
        count = 0

        while current and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        return prev, start, current

    def ant_army(self, group): 
        if group <= 0:
            return self
        
        dummy = Node(None)
        dummy.next = self.head
        prev_group_tail = dummy
        current = self.head
        group_count = 0

        while current:
            group_count += 1
            count = 0
            temp = current
            while temp and count < group:
                temp = temp.next
                count += 1

            if group_count % 2 == 1:
                new_head, new_tail, next_group_start = self.reverse_group(current, count)
                prev_group_tail.next = new_head
                prev_group_tail = new_tail
                current = next_group_start
            else:
                prev_group_tail.next = current
                for _ in range(count):
                    prev_group_tail = current
                    current = current.next

        self.head = dummy.next
        return self

L = LinkedList()
print(" *** Ant Army ***")
total_ant, group = input("Input : ").split(",")
total_ant = total_ant.split(" ")
for ant in total_ant:
    L.append(ant)
print("Before :", L)
print("After :", L.ant_army(int(group)))