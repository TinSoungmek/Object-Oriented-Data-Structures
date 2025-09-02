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

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
        return root

    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level+1)
            print('     ' * level, node)
            self.printTree(node.left, level+1)

    def find_paths(self):
        """หา path ทั้งหมดจาก root ถึงทุก node"""
        all_paths = []
        def dfs(node, path, total):
            if not node:
                return
            path.append(node.data)
            total += node.data
            if len(path) > 1:  # path ต้องมีอย่างน้อย 2 node
                all_paths.append((path[:], total))
            dfs(node.left, path, total)
            dfs(node.right, path, total)
            path.pop()
        dfs(self.root, [], 0)
        return all_paths

    def remove_path(self, path):
        """ลบ path นี้ออกจาก tree โดยตัด node ปลายออก"""
        def _remove(root, depth):
            if not root:
                return None
            if depth == len(path)-1 and root.data == path[depth]:
                return None  # ตัด node ปลาย
            if depth+1 < len(path):
                if path[depth+1] < root.data:
                    root.left = _remove(root.left, depth+1)
                elif path[depth+1] > root.data:
                    root.right = _remove(root.right, depth+1)
                else:
                    root.left = _remove(root.left, depth+1)
                    root.right = _remove(root.right, depth+1)
            return root
        self.root = _remove(self.root, 0)

    def process_condition(self, cond, val):
        paths = self.find_paths()
        removed = []
        for path, total in paths:
            if cond == "L" and total < val:
                removed.append((path, total))
                self.remove_path(path)
            elif cond == "EQ" and total == val:
                removed.append((path, total))
                self.remove_path(path)
            elif cond == "M" and total > val:
                removed.append((path, total))
                self.remove_path(path)

        if removed:
            if cond == "L":
                print(f"Removing paths where the sum is less than {val}:")
            elif cond == "EQ":
                print(f"Removing paths where the sum is equal to {val}:")
            else:
                print(f"Removing paths where the sum is greater than {val}:")
            for i, (p, s) in enumerate(removed, 1):
                print(f"{i}) {'->'.join(map(str, p))} = {s}")
        print("--------------------------------------------------")
        print("(City A) After the war:")
        self.printTree(self.root)


T = BST()
city,army = input("Enter <Create City A (BST)>/<Create conditions and deploy the army>: ").split("/")
for i in city.split():
    T.insert(int(i))

print("(City A) Before the war:")
T.printTree(T.root)
print("--------------------------------------------------")
for cmd in army.split(","):
    cond, num = cmd.split()
    num = int(num)
    T.process_condition(cond, num)
