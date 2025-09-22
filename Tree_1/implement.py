class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self._insert(self.root,data)

    def _insert(self,node,data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert(node.left,data)
        else:
            node.right = self._insert(node.right,data)
        return node

    def print_tree(self,node,level = 0):
        if node:
            self.print_tree(node.right,level+1)
            print('     ' * level, node)
            self.print_tree(node.left,level+1)
        
    def pre_order(self,node):
        result = ""
        if node:
            result += str(node.data) + " "
            result += self.pre_order(node.left)
            result += self.pre_order(node.right)
        return result
    
    def in_order(self,node):
        result = ""
        if node:
            result += self.in_order(node.left)
            result += str(node.data) + " "
            result += self.in_order(node.right)
        return result

    def post_order(self,node):
        result = ""
        if node:
            result += self.post_order(node.left)
            result += self.post_order(node.right)
            result += str(node.data) + " "
        return result
    
    def delete_node(self,node,key):
        if node is None:
            return node
        
        if key < node.data:
            node.left = self.delete_node(node.left,key)
        elif key > node.data:
            node.right = self.delete_node(node.right,key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self.find_min(node.right)
            node.data = temp.data
            node.right = self.delete_node(node.right,temp.data)
        return node

    def find_min(self,node):
        while node.left:
            node = node.left
        return node
    
    def Breadth_first(self):
        q = Queue()
        q.enQ(self.root)
        result = ""
        while q.is_empty() == False:
            n = q.deQ()
            result += str(n.data) + " "
            if n.left:
                q.enQ(n.left)
            if n.right:
                q.enQ(n.right)
        return result

class Queue:
    def __init__(self):
        self.list = []

    def enQ(self,i):
        self.list.append(i)

    def deQ(self):
        return self.list.pop(0)
    
    def is_empty(self):
        return self.list == []
        


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)
T.print_tree(T.root)
print(f"Pre_Order : {T.pre_order(T.root)}")
print(f"In_Order : {T.in_order(T.root)}")
print(f"Post_Order : {T.post_order(T.root)}")
T.delete_node(T.root,4)
T.print_tree(T.root)
print(T.Breadth_first())

