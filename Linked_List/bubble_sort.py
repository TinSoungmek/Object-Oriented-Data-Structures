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

    def bubble_sort(self):
        swapped = True
        while swapped:
            swapped = False
            cur = self.head
            prev = None
            while cur and cur.next:
                next = cur.next
                if cur.value > next.value:
                    print(f"Swapping {cur.value} and {next.value}")
                    swapped = True
                    if prev is None:
                        cur.next = next.next
                        next.next = cur
                        self.head = next
                        prev = self.head
                    else :
                        cur.next = next.next
                        next.next = cur
                        prev.next = next
                        prev = next
                    print(f"list: {self}\n")
                else:
                    prev = cur
                    cur = cur.next
                    
                
L = Linkedlist()
inp = input("Input List: ").split("->")
for i in inp:
    L.append(int(i))
print(f"Before : {L}")
L.bubble_sort()
print(f"After : {L}")