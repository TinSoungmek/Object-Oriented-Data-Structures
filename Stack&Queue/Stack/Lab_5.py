class Stack:

    def __init__(self, capacity = None, list = None,):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.capacity = capacity

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def input_car_soi(self,car):
        if car == "0":
            self.items = []
        else:
            for i in car.split(","):
                i = int(i)
                self.push(i)

    def find_car_in_soi(self,carNumber):
        for i in self.items:
            if i == carNumber:
                return True
            return False
        
    def oper(self,operation,carNumber):
        if operation == "arrive":
            for item in stackA.items:
                if item == carNumber:
                    return f"car {carNumber} already in soi"

            if stackA.capacity > stackA.size():
                stackA.push(carNumber)
                return f"car {carNumber} arrive! : Add Car {carNumber}"
            else:
                return f"car {carNumber} cannot arrive : Soi Full"
        else:
            if stackA.items == []:
                return f"car {carNumber} cannot depart : Soi Empty"
            
            elif self.find_car_in_soi(carNumber):
                for _ in range (stackA.size()):
                    if stackA.peek() == carNumber:
                        stackA.items.pop()
                        for _ in range (stackB.size()):
                            stackA.push(stackB.pop())
                        return f"car {carNumber} depart ! : Car {carNumber} was remove"
                    else:
                        stackB.push(stackA.items.pop())

            else:
                return f"car {carNumber} cannot depart : Dont Have Car {carNumber}"

print("******** Parking Lot ********")
capacity,carSoiA,operation,carNumber = input("Enter max of car,car in soi,operation : ").split(" ")

stackA = Stack(int(capacity))
stackB = Stack()

stackA.input_car_soi(carSoiA)

print(stackA.oper(operation,int(carNumber)))
print(stackA.items)