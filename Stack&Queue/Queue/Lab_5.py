class Queue:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        if not self.isEmpty():
            return self.items[0].pop(0)

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def update_queue(self,sub_queue):
        for i in range(len(self.items)):
            while str(self.items[i][0]) in sub_queue:
                self.items[i] = sub_queue
        return self.items
    
    def manage_queue(self, data):
        output = []
        queueOne = Queue()
        queueTwo = Queue()
        queueThree = Queue()
        
        for item in data:
            if "en" in item:
                word,value = item.split(" ")
                if value[0] == "1":
                    value = int(value)
                    if queueOne.isEmpty():
                        queueOne.enQueue(value)
                        self.enQueue(queueOne.items)
                    else:
                        queueOne.enQueue(value)
                        self.update_queue(queueOne.items)
                    
                elif value[0] == "2":
                    value = int(value)
                    if queueTwo.isEmpty():
                        queueTwo.enQueue(value)
                        self.enQueue(queueTwo.items)
                    else:
                        queueTwo.enQueue(value)
                        self.update_queue(queueTwo.items)

                else:
                    value = int(value)
                    if queueThree.isEmpty():
                        queueThree.enQueue(value)
                        self.enQueue(queueThree.items)
                    else:
                        queueThree.enQueue(value)
                        self.update_queue(queueThree.items)

                output.append(f"Enqueued: {value}")
                output.append(f"Queue state: {self.items}")
                
                
            elif "de" in item:
                if not self.isEmpty():
                    value = self.deQueue()
                    if self.items[0] == []:
                        self.items = [x for x in self.items if x]
                    output.append(f"Dequeued: {value}")
                    output.append(f"Queue state: {self.items}")
                else:
                    output.append("Queue is empty")
        return "\n".join(output)

print(" ***Queue of Queue of Queue of ...*** ")
data= input("Enter Input : ").split(",")
queue = Queue()
print(queue.manage_queue(data))