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
    
    def operation(self,input):
        output = []
        result = []
        for _ in range (len(input)):
            output.append(-1)
        
        for i in range (len(input)):
            while not self.isEmpty() and input[self.peek()] < input[i]:
                result.append(f"input[{i}]({input[i]}) is greater than input[top of stack]({input[self.peek()]})")
                index = self.pop()
                result.append("Stack pop")
                output[index] = input[i]
                result.append(f"Output: {output}")
            self.push(i)
            result.append(f"Stack push {i} index of {input[i]}")
        result.append(f"Output: {output}")
        return "\n".join(result)
        
print("*****Big leg on the right side*****")
data = input("Enter input: ").split(" ")
index = Stack()
print(index.operation(list(map(int,data))))
