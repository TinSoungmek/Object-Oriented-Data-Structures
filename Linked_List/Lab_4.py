class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.angry = 0
        self.alive = True
    
    def __str__(self):
        s = "Current Ant List:"
        current_node = self.head
        if current_node == None:
            s += " Empty"

        while current_node:
            s += " " + current_node.value
            current_node = current_node.next
        
        return s
    
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def create_ant(self,ant):
        worker,army = ant.split(" ")

        for i in range (int(worker)):
            self.append(f"W{i+1}")

        for i in range (int(army)):
            self.append(f"A{i+1}")

    def carry_food(self,num):
        current_node = self.head
        s = "Food carrying mission :"
        if current_node == None:
            s += " Empty"

        while num > 0 and current_node:
            if "W" in current_node.value:
                num -= 2
                s += " " + current_node.value
                self.head = current_node.next
            elif "A" in current_node.value:
                num -= 5
                s += " " + current_node.value
                self.head = current_node.next
            current_node = current_node.next
        if num > 0 :
            self.angry += 1
            if self.angry == 3:
                return s + "\nThe food load is incomplete!\nQueen is angry! ! !\n**The queen is furious! The ant colony has been destroyed**"
            return s + "\nThe food load is incomplete!\nQueen is angry! ! !"
        return s
    

    def fight_enermy(self, num):
        s = "Attack mission :"
        current_node = self.head
        prev_node = None

        while num > 0 and current_node:
            if "A" in current_node.value:
                num -= 10
                s += " " + current_node.value
                if prev_node is None:
                    self.head = current_node.next
                    current_node = self.head
                else:
                    prev_node.next = current_node.next
                    current_node = prev_node.next
            else:
                prev_node = current_node
                current_node = prev_node.next

        current_node = self.head
        prev_node = None
        while num > 0 and current_node:
            if "W" in current_node.value:
                num -= 5
                s += " " + current_node.value
                if prev_node is None:
                    self.head = current_node.next
                    current_node = self.head
                else:
                    prev_node.next = current_node.next
                    current_node = prev_node.next
            else:
                prev_node = current_node
                current_node = current_node.next

        if num > 0:
            self.alive = False
            return s + "\nAnt nest has fallen!"
        return s



    def show_ants_remaining(self):
        if self.alive:
            current_node = self.head
            s_worker = "-> Remaining worker ants:"
            s_army = "-> Remaining soldier ants:"
            while current_node:
                if "W" in current_node.value:
                    s_worker += " " + current_node.value
                    current_node = current_node.next
                elif "A" in current_node.value:
                    s_army += " " + current_node.value
                    current_node = current_node.next
            if s_worker == "-> Remaining worker ants:":
                s_worker += " Empty"
            if s_army == "-> Remaining soldier ants:":
                s_army += " Empty"

            return s_worker,s_army
        return "error"
    
    def add_worker_ants(self,num):
        self.create_ant(f"{num} 0")
        
    def add_army_ants(self,num):
        self.create_ant(f"0 {num}")

L = LinkedList()
print("***This colony is our home***")
ant,action = input("Enter input : ").split("/")
L.create_ant(ant)
print(L,"\n")
total_mission = action.split(",")
for mission in total_mission:
    if mission[0] == "C":
        print(L.carry_food(int(mission[2:])))
    elif mission[0] == "F":
        print(L.fight_enermy(int(mission[2:])))
    elif mission[0] == "S":
        if L.show_ants_remaining() == "error":
            break
        work,army = L.show_ants_remaining()
        print(work)
        print(army)
    elif mission[0] == "W":
        L.add_worker_ants(int(mission[2:]))
    elif mission[0] == "A":
        L.add_army_ants(int(mission[2:]))