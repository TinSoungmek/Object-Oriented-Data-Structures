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
            return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def operation(self,minute,people):
        listFinal = []
        cashier1 = 1
        cashier2 = 1
        for i in people:
            self.enQueue(i)

        for i in range (minute):
            if not queue1.isEmpty():
                if cashier1 == 3:
                    queue1.deQueue()
                    cashier1 = 1
                else: 
                    cashier1 += 1

            if not queue2.isEmpty():
                if cashier2 == 2:
                    queue2.deQueue()
                    cashier2 = 1
                else: 
                    cashier2 += 1

            if not self.isEmpty():
                if queue1.size() < 5:
                    queue1.enQueue(self.deQueue())
                elif queue2.size() < 5:
                    queue2.enQueue(self.deQueue())

            listFinal.append(i+1)
            listFinal.append(self.items.copy())
            listFinal.append(queue1.items.copy())
            listFinal.append(queue2.items.copy())

        return listFinal

    

people,minute = input("Enter people and time : ").split(" ")
queueMain = Queue()
queue1 = Queue()
queue2 = Queue()
result = queueMain.operation(int(minute),list(people))

for i in range(0,len(result),4):
    print(result[i],result[i+1],result[i+2],result[i+3])


