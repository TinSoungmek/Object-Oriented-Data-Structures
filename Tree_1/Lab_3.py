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
        return self.root
    
    def _insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self._insert(root.left, data)
            elif data > root.data:
                root.right = self._insert(root.right, data)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        
    def sum_of_tree(self, node):
        sum = 0
        
        if node is None:
            return 0
        
        sum += node.data
        sum += self.sum_of_tree(node.left)
        sum += self.sum_of_tree(node.right)

        return sum
    
    def update_value(self, node, k):
        if node is None:
            return
        
        if node.data > k:
            node.data = node.data*k
        
        self.update_value(node.left, k)
        self.update_value(node.right, k)

T = BST()
print("**Sum of tree**")
inp,k = input('Enter input : ').split("/")
inp = inp.split(" ")
for i in inp:
    T.insert(int(i))
print("\nTree before:")
T.printTree(T.root)
print(f"Sum of all nodes = {T.sum_of_tree(T.root)}")
T.update_value(T.root, int(k))
print("\nTree after:")
T.printTree(T.root)
print(f"Sum of all nodes = {T.sum_of_tree(T.root)}")