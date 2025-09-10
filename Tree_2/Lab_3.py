class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = self.setHeight()

    def setHeight(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a,b)
        return self.height
    
    def getHeight(self, node):
        if not node:
            return -1
        return node.height
    
    def balanceValue(self):
        return self.getHeight(self.left) - self.getHeight(self.right)


    def __str__(self):
        return str(self.data)
    
class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root
    
    def _insert(self, root, data):
        if not root:
            return Node(data)
        else:
            if data < root.data:
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
            root = self.rebalance(root)
            return root

    def left_rotate(self, root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot
    
    def right_rotate(self, root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot
    
    def rebalance(self, root):
        if root == None:
            return root
        balance = root.balanceValue()
        if balance == -2:
            if root.right.balanceValue() == 1:
                root.right = self.left_rotate(root.right)
            root = self.right_rotate(root)
        elif balance == 2:
            if root.left.balanceValue() == -1:
                root.left = self.right_rotate(root.left)
            root = self.left_rotate(root)
        root.setHeight()
        return root
    
    def print_tree(self, node, level = 0):
        if node:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

    def max_sum(self, node, path = None):
        if not self.root:
            return 0
        if not path:
            path = []
        if node:
            path.append(node.data)
            return self.max_sum(node.right, path.copy()) if node.right else self.max_sum(node.left, path.copy())
        return path, sum(path)

avl = AVL()
inp = input("Enter tree nodes: ").split()
for item in inp:
    avl.root = avl.insert(int(item))
avl.print_tree(avl.root)
path, length = avl.max_sum(avl.root)
path_sum = ' + '.join(map(str, path))
print(f"\nPath with maximum sum: {path_sum} = {length}")