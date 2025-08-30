class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        

    def addHead(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def search(self, item):
        current_node = self.head
        while current_node:
            if item == current_node.value :
                return f"Found {item} in"
            current_node = current_node.next
        return f"Not Found {item} in"

    def index(self, item):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == item:
                return index
            index += 1
            current_node = current_node.next
        return -1
        
    def size(self):
        current_node = self.head
        size = 0
        while current_node:
            size += 1
            current_node = current_node.next
        return size
        

    def pop(self, pos):
        current_node = self.head
        index = 0
        if self.head == None:
            return "Out of Range"
        if pos == 0:
            self.head = self.head.next
            return "Success"
        else:
            while current_node != None and index < pos - 1:
                index += 1
                current_node = current_node.next
            
            if current_node == None or current_node.next == None:
                return "Out of Range"
            else:
                current_node.next = current_node.next.next
                return "Success"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1}".format(L.search(i[3:]), L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)