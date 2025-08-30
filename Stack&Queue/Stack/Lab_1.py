class Stack:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def calculate(self,data):
        number = list(map(int,data))
        for i in number:
            if self.isEmpty():
                self.push(i)
            elif self.peek() + i == 5 or self.peek() + i == 10 or \
            self.peek() - i == 5 or self.peek() - i == 10:
                self.push(i)
            else:
                continue
        return " ".join(str(i) for i in self.items)
    
print("***Always 5 or 10***")
data = input("Enter Input : ").split()
stack = Stack()
print(f"Output : {stack.calculate(data)}")