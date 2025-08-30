class Queue:

    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,i):
        self.items.append(i)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def operation(self,book,act):
        book = book.split(" ")
        act = act.split(",")
        for i in book:
            self.enQueue(i)

        for i in act:
            if "E" in i:
                char,value = i.split(" ")
                self.enQueue(value)
            elif "D" in i:
                self.deQueue()

        for i in range (self.size()):
            for j in range (self.size()):
                if i == j:
                    continue
                else:
                    if self.items[i] == self.items[j]:
                        return "Duplicate"
        return "NO Duplicate"

bookAvaliable,action = input("Enter Input : ").split("/")
queue = Queue()

print(queue.operation(bookAvaliable,action))