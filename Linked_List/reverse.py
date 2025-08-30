class Node:

    def __init__(self,value):
        self.value = value
        self.next = None
    
class Linkedlist:

    def __init__(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        if self.head == None:
            return "Empty"
        cur,s = self.head,str(self.head.value)
        cur = cur.next
        while cur :
            s += "->" + str(cur.value)
            cur = cur.next
        return s

    def append(self,item):
        cur_node = self.head
        new_node = Node(item)
        if cur_node == None:  
            self.head = new_node
            return
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def reverse(self):
        prev = None
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node
        self.head = prev

L = Linkedlist()
inp = input("input = ").split(" ")
for i in inp:
    L.append(i)
print(L)
L.reverse()
print(L)