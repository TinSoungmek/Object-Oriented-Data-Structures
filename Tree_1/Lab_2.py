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
    
    def inorder(self):
        return self._inorder(self.root)
    
    def _inorder(self, root):
        result = ""
        if root:
            result += self._inorder(root.left)
            result += str(root.data) + " "
            result += self._inorder(root.right)
        return result
    
    def summation(self, node, target):
        if node is None:
            return False
        
        target -= node.data

        if node.left is None and node.right is None:
            return target == 0

        return (self.summation(node.left, target) or
                self.summation(node.right, target))
    
T = BST()
inp,target = input('Enter the values to insert into BST and target sum : ').split(" / ")
inp = inp.split(" ")
for i in inp:
    T.insert(int(i))
print(f"Inorder Traversal of BST : {T.inorder()}")
print(f"Path with sum {target} exists : {T.summation(T.root,int(target))}")