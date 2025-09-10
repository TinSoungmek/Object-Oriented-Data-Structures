class AVLTree:

    class AVLNode:

        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a,b)
            return self.height

        def getHeight(self, node):
            return -1 if node == None else node.height

        def balanceValue(self):      
            return self.getHeight(self.left) - self.getHeight(self.right)

    def __init__(self, root = None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self,root, data):
        if root is None:
            return self.AVLNode(data)
        else:
            if int(data) < int(root.data):
                root.left = self._add(root.left, data)
            else:
                root.right = self._add(root.right, data)

        root.setHeight() 
        root = self.rebalance(root)
        return root

    def rebalance(self, root):
        if root == None:
            return root
        balance = root.balanceValue()
        if balance == -2:
            if root.right.balanceValue() == 1:
                root.right = self.rotateLeftChild(root.right)
            root = self.rotateRightChild(root)
        elif balance == 2:
            if root.left.balanceValue() == -1:
                root.left = self.rotateRightChild(root.left)
            root = self.rotateLeftChild(root)
        root.setHeight()
        return root

    def rotateLeftChild(self, root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot
    
    def rotateRightChild(self, root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self,root):
        result = ""
        if root:
            result += self._postOrder(root.left)
            result += self._postOrder(root.right)
            result += str(root) + " "
        return result
    
    def printTree(self):
        self._printTree(self.root)
        print()

    def _printTree(self, node , level=0):
        if not node is None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self._printTree(node.left, level + 1)

avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:

    if i[:2] == "AD":
        avl1.add(i[3:])

    elif i[:2] == "PR":
        avl1.printTree()

    elif i[:2] == "PO":
        print(f"AVLTree post-order : {avl1.postOrder()}")