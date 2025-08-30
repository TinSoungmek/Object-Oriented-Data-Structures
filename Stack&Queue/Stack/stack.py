class Stack:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[-1]
    
    def match(self,op,cl):
        open = "[{("
        close = "]})"
        return open.index(op) == close.index(cl)
    
    def parenthesis(self,item):
        error = False
        for i in range (len(item)):
            if item[i] in "[{(":
                self.push(item[i])
            elif item[i] in "]})":
                if self.size() > 0:
                    if self.match(self.peek(),item[i]):
                        self.pop()
                    else:
                        error = True
                        break
                else:
                    error = True
                    break
            else:
                continue
        if self.size() > 0:
            error = True
            
        if error:
            print("Not Match")
        else:
            print("Match")
        

data = input("Enter Input :")
stack = Stack()
stack.parenthesis(data)