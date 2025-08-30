class Queue:

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    
    def num_to_text(self,list):
        listActLo = []
        for item in list:
            activity,location = item.split(":")

            if activity == "0":
                activity = "Eat"
            elif activity == "1":
                activity = "Game"
            elif activity == "2":
                activity = "Learn"
            else:
                activity = "Movie"

            if location == "0":
                location = "Res."
            elif location == "1":
                location = "ClassR."
            elif location == "2":
                location = "SuperM."
            else:
                location = "Home"

            listActLo.append(f"{activity}:{location}")
        return listActLo

    def calculate_point(self,myPoint,yourPoint):
        point = 0
        for myItem,yourItem in zip(myPoint.items,yourPoint.items):
            myAct,myLo = myItem.split(":")
            yourAct,yourLo = yourItem.split(":")
            if myAct == yourAct and myLo != yourLo:
                point += 1
            elif myAct != yourAct and myLo == yourLo:
                point += 2
            elif myAct == yourAct and myLo == yourLo:
                point += 4
            else:
                point -= 5
        
        if point >= 7: return f"Yes! You're my love! : Score is {point}."
        elif 0 < point < 7: return f"Umm.. It's complicated relationship! : Score is {point}."
        else: return f"No! We're just friends. : Score is {point}."

    def operation(self, list):
        listResult = []
        myQueue = Queue()
        yourQueue = Queue()

        for i in list:
            my,your = i.split(" ")
            myQueue.enQueue(my)
            yourQueue.enQueue(your)

        listResult += [
            f"My   Queue = {', '.join(myQueue.items)}",
            f"Your Queue = {', '.join(yourQueue.items)}",
            f"My   Activity:Location = {', '.join(myQueue.num_to_text(myQueue.items))}",
            f"Your Activity:Location = {', '.join(yourQueue.num_to_text(yourQueue.items))}",
            self.calculate_point(myQueue,yourQueue)
        ] 
        
        return "\n".join(listResult)

data = input("Enter Input : ").split(",")
queue = Queue()
print(queue.operation(data))