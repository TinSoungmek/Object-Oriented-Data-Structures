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

avl1 = AVL()
avl2 = AVL()
inp = input("Enter Tree1/Tree2 : ").split("/")
print("Tree 1")
for item in inp[0].split():
    avl1.root = avl1.insert(avl1.root, int(item))
avl1.print_tree(avl1.root)
print("\nTree 2")
for item in inp[1].split():
    avl2.root = avl2.insert(avl2.root, int(item))
avl2.print_tree(avl2.root)
print(f"\nSame Tree" if compare(avl1.root, avl2.root) else "\nDifferent Tree")