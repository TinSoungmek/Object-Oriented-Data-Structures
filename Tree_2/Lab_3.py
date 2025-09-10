class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = self.setHeight()

    def setHeight(self):
        lheight = self.get_height(self.left)
        rheight = self.get_height(self.right)
        self.height = 1 + max(lheight, rheight)
        return self.height
    
    def get_height(self, node):
        if not node:
            return -1
        return node.height
    
    def balanceVal(self):
        lheight = self.get_height(self.left)
        rheight = self.get_height(self.right)
        return lheight - rheight

    def __str__(self):
        return str(self.data)
    
class AVL:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return Node(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            root = self.rebalance(root)
            return root

    def left_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        x.setHeight()
        y.setHeight()
        return y
    
    def right_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.setHeight()
        y.setHeight()
        return y
    
    def rebalance(self, x):
        if not x:
            return x
        balance = x.balanceVal()
        if balance == -2:
            if x.right.balanceVal() == 1:
                x.right = self.left_rotate(x.right)
            x = self.right_rotate(x)
        elif balance == 2:
            if x.left.balanceVal() == -1:
                x.left = self.right_rotate(x.left)
            x = self.left_rotate(x)
        x.setHeight()
        return x
    
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
    avl.root = avl.insert(avl.root, int(item))
avl.print_tree(avl.root)
path, length = avl.max_sum(avl.root)
path_sum = ' + '.join(map(str, path))
print(f"\nPath with maximum sum: {path_sum} = {length}")