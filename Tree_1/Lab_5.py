class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node
    
    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level+1)
            print('     ' * level, node)
            self.printTree(node.left, level+1)

    def find_all_path(self, path=[]):
        return self._find_all_path(self.root, path)
    
    def _find_all_path(self, node, path):
        if node is None:
            return []
        current_path = path + [node.data]
        result = [current_path]

        result.extend(self._find_all_path(node.left, current_path))
        result.extend(self._find_all_path(node.right, current_path))

        return result

    def remove_by_path(self, path):
        if not path or self.root is None:
            return False
        
        if len(path) == 1:
            if self.root.data == path[0] and self.root.left is None and self.root.right is None:
                self.root = None
                return True
            return False
        
        self.root, success = self._remove_by_path(self.root, path, 0)
        return success
    
    def _remove_by_path(self, node, path, index):
        if node is None or index >= len(path) or node.data != path[index]:
            return node, False
        
        if index == len(path) - 1:
            if node.left is None and node.right is None:
                return None, True
            return node, False
        
        next_data = path[index + 1]
        left_removed = False
        right_removed = False

        if node.left and node.left.data == next_data:
            node.left, left_removed = self._remove_by_path(node.left, path, index + 1)

        if not left_removed and node.right and node.right.data == next_data:
            node.right, right_removed = self._remove_by_path(node.right, path, index + 1)

        return node, left_removed or right_removed

    def print_path(self,path):
        return ("->".join(map(str, path)))

city, cond = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ").split('/')
T = BST()
for n in city.split():
    T.insert(int(n))
print("(City A) Before the war:")
T.printTree(T.root)
for condition in cond.split(','):
    print("--------------------------------------------------")
    all_path = T.find_all_path()
    fight_path = []
    success_fight_path = []
    char, k = condition.split()
    k = int(k)
    finish_loop = False

    if char == 'L':
        print(f"Removing paths where the sum is less than {k}:")
        for path in all_path:
            power = sum(path)
            if power < k:
                fight_path.append(path)

    if char == 'EQ':
        print(f'Removing paths where the sum is equal to {k}:')
        for path in all_path:
            power = sum(path)
            if power == k:
                fight_path.append(path)

    if char == 'M':
        print(f'Removing paths where the sum is greater than {k}:')
        for path in all_path:
            power = sum(path)
            if power > k:
                fight_path.append(path)
                

    while not finish_loop:
        finish_loop = True
        for path in fight_path:
            success = T.remove_by_path(path)
            if success:
                fight_path.remove(path)
                success_fight_path.append(path)
                finish_loop = False
                break

    if success_fight_path:
        for i in range(len(success_fight_path)):
            print(f"{i+1}) {T.print_path(success_fight_path[i])} = {sum(success_fight_path[i])}")

    else:
        print("No paths were removed.")

    print('--------------------------------------------------')
    print("(City A) After the war:")
    T.printTree(T.root)
    if T.root is None:
        print("City A has fallen!")
        break