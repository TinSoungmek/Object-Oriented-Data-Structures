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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def find_path(self, node, treasure, escape, path):
        global status

        if node is None:
            return False
        
        path.append(node.data)
        
        if node.data == treasure:
            status = 1
            print("Found Treasure !!!")
        
        if node.data == escape and status == 1:
            print("Found Escape !!!")
            return True
            
        print("❌", " -> ".join(map(str, path)))
        
        if (self.find_path(node.left, treasure, escape, path) or
        self.find_path(node.right, treasure, escape, path)):
            return True
        
        path.pop()
        return False

    def get_node(self, node, target):
        if node is None:
            return None
        if node.data == target:
            return node
        elif target < node.data:
            return self.get_node(node.left, target)
        else:
            return self.get_node(node.right, target)


T = BST()
inp,treasure,escape = input('Enter Input : ').split("/")
inp = inp.split(" ")
path = []
status = 0

for i in inp:
    T.insert(int(i))
T.printTree(T.root)
print("-------------------------------------------------")
if T.find_path(T.root, int(treasure), int(escape), path):
    print("✅", " -> ".join(map(str, path)))
    print(">>> Mission Complete <<<")

else:
    print(">>> Mission Failed <<<")