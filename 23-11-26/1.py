class Node:
    def _init_(self,value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def _init_(self):
        self.root = None
        self.count=0

    def insert(self,newNode):
        if self.root == None:
            self.root = newNode
            return
        else:
            temp = self.root
            while True:
                if newNode.data < temp.data:
                    if temp.left is None:
                        temp.left = newNode
                        return
                    else:
                        temp = temp.left
                else:                   #right subtree
                    if temp.right is None:
                        temp.right = newNode
                        return
                    else:
                        temp = temp.right

    def inorder(self,temp):          #recursive
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.count+=1
            self.inorder(temp.right)


    def find_minmax(self, rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("\n Min value", temp.data)
        temp=rt
        while temp.right:
            temp=temp.right
        print("\n Max value", temp.data)

btree = BST()
btree.insert(Node(100))
btree.insert(Node(10))
btree.insert(Node(450))
btree.insert(Node(4))
btree.insert(Node(65))
btree.insert(Node(300))
btree.insert(Node(500))
btree.insert(Node(50))
btree.inorder(btree.root)
print("\nTotal nodes:",btree.count)
print("\nPreorder:")
btree.preorder(b1.root)
print("\nPostorder:")
btree.postorder(b1.root)