class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = [] 
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def fine_plate(self, target):
        plates = [25, 20, 15, 10, 5, 2.5, 1.25]
        result = []
        for plate in plates:
            while sum(result) + plate <= target and len(result) < 5:
                result.append(plate)
        return sorted(result,reverse=True) if sum(result) == target else None

    def operation_plate(self, old, new):
        action = []
        mismatch_index = 0
        for i in range(min(len(old), len(new))):
            if old[i] != new[i]:
                break
            mismatch_index += 1

        for i in range(len(old) - 1, mismatch_index - 1, -1):
            removed = stack.pop()
            action.append(f"PO:{int(removed) if removed == int(removed) else removed}")

        for i in range(mismatch_index, len(new)):
            stack.push(new[i])
            action.append(f"PU:{int(new[i]) if new[i] == int(new[i]) else new[i]}")

        return ' '.join(action)



    def print_bar(self, new, actions, weight):
        dashes = '-' * (5 - len(new))
        plates = ''.join(f"[{int(i)}]" if i == int(i) else f"[{i}]" for i in new)
        reverse = ''.join(f"[{int(i)}]" if i == int(i) else f"[{i}]" for i in reversed(new))
        bar =  f"{dashes}{reverse}|======|{plates}{dashes}"

        has_float = any(isinstance(i,float) for i in new)

        if actions == '':
            if has_float:
                print(f"{bar} => {weight:.1f} KG.")
            else:
                print(f"{bar} => {int(weight)} KG.")    
        else:
            if has_float:
                print(f"{actions} => {bar} => {weight:.1f} KG.")
            else:
                print(f"{actions} => {bar} => {int(weight)} KG.") 


stack = Stack()
weights = list(map(float, input("Enter needed weight(s): ").split()))
for weight in weights:
    need = (weight - 20) / 2
    new_plate = stack.fine_plate(need)
    if new_plate is None:
        print(f"It's impossible to achieve the weight you want({int(weight) if weight == int(weight) else weight}).")
        break
    actions = stack.operation_plate(stack.items, new_plate)
    stack.print_bar(new_plate,actions,weight)