class Queue:

    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        if self.isEmpty():
            return "-1"
        return f"{self.items.pop(0)} 0"

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def operation(self,data):
        listResult = []
        for i in data:
            if "E" in i:
                e,value = i.split(" ")
                value = int(value)
                self.enQueue(value)
                listResult.append(self.size())
            elif "D" in i:
                listResult.append(self.deQueue())
        if not self.isEmpty():
            listResult.append(" ".join(str(item) for item in self.items))
        else :
            listResult.append("Empty")

        return "\n".join(str(result) for result in listResult)
    
data = input("Enter Input : ").split(",")
queue = Queue()
print(queue.operation(data))

