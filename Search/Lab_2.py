class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def append(self,item):
        if self.head is None:
            self.head = Node(item)
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = Node(item)

    def size(self):
        cur_node = self.head
        size = 0
        while cur_node:
            size += 1
            cur_node = cur_node.next
        return size
    
    def addHead(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
    
    def search(self,key):
        global cost
        found = False
        cur_node = self.head
        if cur_node.value == key:
            print(f"Search {key} -> found at 1 move to front ->  {L}")
            cost += 1
        else:
            count = 1
            while cur_node.next:
                count += 1
                next_node = cur_node.next
                if next_node.value == key:
                    cur_node.next = next_node.next
                    next_node.next = self.head
                    self.head = next_node

                    cost += count
                    found = True
                    print(f"Search {key} -> found at {count} move to front ->  {L}")

                else:
                    cur_node = cur_node.next

            if not found:
                if key in counter:
                    self.addHead(key)
                    counter.remove(key)
                    cost += 1
                    print(f"Search {key} -> add new book ->  {L}")
                else:
                    counter.append(key)
                    cost += self.size() + 1
                    print(f"Search {key} -> not found -> {L}")

L = LinkedList()
counter = []
print("This is your BOOK!!!")
inp,out = input("Enter input: ").split("/")
cost = 0
for i in inp.split(' '):
    L.append(i)

for i in out.split(' '):
    L.search(i)

print(f"\nFinal books: {L}")
print(f"Total cost: {cost}")