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
            print(f"{'    ' * level}{node}")
            self.print_tree(node.left, level + 1)


def compare(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if tree1.data != tree2.data:
        return False
    return compare(tree1.left, tree2.left) and compare(tree1.right, tree2.right)

Tree1 = AVL()
Tree2 = AVL()
Tree1_inp, Tree2_inp = (input("Enter Tree1/Tree2 : ")).split("/")
Tree1_inp = Tree1_inp.split()
Tree2_inp = Tree2_inp.split()

for data in Tree1_inp:
    Tree1.insert(int(data))

for data in Tree2_inp:
    Tree2.insert(int(data))

print("Tree 1")    
Tree1.print_tree(Tree1.root)
print()

print("Tree 2")
Tree2.print_tree(Tree2.root)
print()

if compare(Tree1.root, Tree2.root):
    print("Same Tree")
else:
    print("Different Tree")