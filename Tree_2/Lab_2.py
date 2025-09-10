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
    
    def balanceValue(self):
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
            if root.left.balanceValue() == 1:
                root.left = self.left_rotate(root.left)
            root = self.right_rotate(root)
        elif balance == 2:
            if root.right.balanceValue() == -1:
                root.right = self.right_rotate(root.right)
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