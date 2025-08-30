class Queue:

    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
        
    def enQueue(self,item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []