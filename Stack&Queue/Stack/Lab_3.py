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
    
    def check_start(self,start):
        if start:
            start = list(map(int,start.split(" ")))
            for i in start:
                if i == 0:
                    continue
                self.push(i)
        else:
            start = None
        return f"\nstart\n{self.items}\n"
    
    def operation(self,action):
        listAction = []
        action = list(action.split(","))
        for i in action:
            if "spawn" in i:
                act,value = i.split(" ")
                self.push(int(value))
                listAction.append(f"spawn an enemy of {value} HP\n{self.items}\n")

            elif "dmg" in i :
                countEnemy = 0
                act,value = i.split(" ")
                value = int(value)
                if value == 0:
                    listAction.append("Invalid number\n")
                else:
                    totalDamage = value
                    while value >= 0:
                        if self.isEmpty():
                            break
                        elif value >= self.peek():
                            value -= self.pop()
                            countEnemy += 1
                        else:
                            x = self.pop() - value
                            self.push(x)
                            break
                    listAction.append(f"deal {totalDamage} damage, killed {countEnemy} enemy\n{self.items}\n")
        if self.isEmpty():
            listAction.append(">>>> Player Wins <<<<")
        return "\n".join(listAction)
    



stack = Stack()
start,action = input("Enter Input : ").split("/")
print(stack.check_start(start))
print(stack.operation(action))
