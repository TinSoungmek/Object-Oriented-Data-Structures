class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = self.set_height()
    
    def __str__(self):
        return str(self.data)
    
    def set_height(self):
        a = self.get_height(self.left)
        b = self.get_height(self.right)
        self.height = 1 + max(a,b)
        return self.height

    def get_height(self,node):
        return -1 if node == None else node.height
    
    def balance_factor(self):
        return self.get_height(self.left) - self.get_height(self.right)
    
class AVL:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self._insert(self.root,data)
        return self.root

    def _insert(self,node,data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert(node.left,data)
        else:
            node.right = self._insert(node.right,data)
        
        # node.set_height()
        node = self.rebalance(node)
        return node
        
    def rebalance(self,node):
        if node is None:
            return node
        balance = node.balance_factor()
        if balance == -2:
            if node.right.balance_factor() == 1:
                node.right = self.left_rotate(node.right)
            node = self.right_rotate(node)
        elif balance == 2:
            if node.left.balance_factor() == -1:
                node.left = self.right_rotate(node.left)
            node = self.left_rotate(node)
        node.set_height()
        return node

    def left_rotate(self,root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.set_height()
        new_root.set_height()
        return new_root

    def right_rotate(self,root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.set_height()
        new_root.set_height()
        return new_root
    
    def printTree(self, node , level=0):
        if not node is None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

    def postOrder(self,root):
        result = ""
        if root:
            result += self.postOrder(root.left)
            result += self.postOrder(root.right)
            result += str(root) + " "
        return result

avl1 = AVL()

inp = input('Enter Input : ').split(',')

for i in inp:

    if i[:2] == "AD":
        avl1.insert(int(i[3:]))
        
    elif i[:2] == "PR":
        avl1.printTree(avl1.root)

    elif i[:2] == "PO":
        print(f"AVLTree post-order : {avl1.postOrder(avl1.root)}")