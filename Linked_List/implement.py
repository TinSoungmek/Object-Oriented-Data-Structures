class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.amount = 0

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
        self.amount += 1
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def addHead(self, item):
        new_node = Node(item)
        self.amount += 1
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def search(self, item):
        cur_node = self.head
        while cur_node:
            if cur_node.value == item:
                return f"Found {item} in"
            cur_node = cur_node.next
        return f"Not Found {item} in"
    
    def index(self, item):
        cur_node = self.head
        count = 0
        while cur_node:
            if cur_node.value == item:
                return count
            count += 1
            cur_node = cur_node.next
        return -1
        
    def size(self):
        return self.amount

    def pop(self, pos):
        cur_node = self.head
        count = 0
        if cur_node == None:
            return "Out of Range"
        elif pos == 0:
            self.head = cur_node.next
            self.amount -= 1
            return "Success"
        
        while cur_node.next and count < pos:
            if count == pos-1:
                cur_node.next = cur_node.next.next
                self.amount -= 1
                return "Success"
            cur_node = cur_node.next
            count += 1
        return "Out of Range"

    def remove_tail(self):
        cur_node = self.head
        if cur_node == None:
            return
        if cur_node.next == None:
            self.head = None
            self.amount -= 1
            return
        while cur_node.next.next:
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next
        self.amount -=1

    def insert(self,item,index):
        cur_node = self.head
        count = 0
        new_node = Node(item)
        while cur_node and count < index:
            if count == index-1:
                new_node.next = cur_node.next
                cur_node.next = new_node
                self.amount += 1
            cur_node = cur_node.next
            count += 1


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
    elif i[:2] == "RT":
        L.remove_tail()
    elif i[:2] == "IS":
        item,index = i[3:].split(" ")
        L.insert(item,int(index))
print("Linked List :", L)