#25-11-26: DSA Practical Assignment 4 - Bhavya Bhat

#Q. 1 E-Commerce Product Search System 
#An e-commerce company maintains product IDs in a BST to enable efficient product searching. 
#Tasks: 
#1. Create a BST using product IDs.  
#Insert the following product IDs:  
#150, 100, 200, 75, 125, 175, 250, 60, 90, 110. 
#2. Display product IDs in ascending order. 
#3. Search for product ID 175 exists. 
#4. Delete product ID 100. 
#5. Display the BST using inorder, preorder, and postorder traversals. 
#6. Find the minimum and maximum product IDs.


# Creating Node class that stores each product ID
class Node:
    def __init__(self, data):
        self.left = None          # Stores left child address
        self.right = None         # Stores right child address 
        self.product_id = data    # Stores product id 


# Creating a Binary Search Tree class
class BST:
    def __init__(self):
        self.root = None          # tree is empty initially 

    # 1. Inserting product IDs into the BST
    def insert(self, new_node):

        # check if the tree is empty, new node becomes the root
        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:

            if new_node.product_id < temp.product_id:

                if temp.left is None:
                    temp.left = new_node
                    return

                else:
                    temp = temp.left
            else:

                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    temp = temp.right


    # 2. Displaying product IDs in ascending order
    def inorder(self, root):
        if root is None: #if the current node is empty then it stops 
            return
        self.inorder(root.left)
        print(root.product_id, end=" ")
        self.inorder(root.right)

    # 5. Preorder traversal 
    def preorder(self, root):
        if root is None:
            return
        print(root.product_id, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    # 5. Postorder traversal 
    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.product_id, end=" ")


    # 3. Searching for a product ID
    def search(self, key):
        temp = self.root
        while temp:
            if temp.product_id == key: #returns true if the product id matches 
                return True
            elif key < temp.product_id:
                temp = temp.left
            else:
                temp = temp.right
        return False


    # Finding the inorder successor during deletion
    def get_successor(self, root):
        temp = root.right
        while temp.left is not None:
            temp = temp.left
        return temp


    # 4. Deleting a product ID from the BST
    def delete_node(self, root, val):

        if root is None: #nothing gets deleted if the node is empty 
            return None
        if val < root.product_id:
            root.left = self.delete_node(root.left, val)
        elif val > root.product_id:
            root.right = self.delete_node(root.right, val)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ = self.get_successor(root)
            root.product_id = succ.product_id
            root.right = self.delete_node(root.right, succ.product_id)

        return root


    # 6. Finding the minimum product ID
    def minimum(self):
        temp = self.root
        if temp is None:
            return None
        while temp.left is not None:
            temp = temp.left
        return temp.product_id


    # 6. Finding the maximum product ID
    def maximum(self):
        temp = self.root
        if temp is None:
            return None
        while temp.right is not None:
            temp = temp.right

        return temp.product_id


# Creating an object for the BST class 
b = BST()

# Enter the choice
print("1. Insert the product ID")
print("2. Display product IDs in ascending order")
print("3. Search for product ID 175")
print("4. Delete product ID 100")
print("5. Display inorder, preorder and postorder")
print("6. Find minimum and maximum product IDs")
print("7. Exit")

while True:
    ch = int(input("\nEnter choice: "))

    if ch == 1:
        b.insert(Node(150))
        b.insert(Node(100))
        b.insert(Node(200))
        b.insert(Node(75))
        b.insert(Node(125))
        b.insert(Node(175))
        b.insert(Node(250))
        b.insert(Node(60))
        b.insert(Node(90))
        b.insert(Node(110))
        print("Product IDs inserted successfully")

    elif ch == 2:
        print("Product IDs in ascending order:")
        b.inorder(b.root)
        print()

    elif ch == 3:
        if b.search(175):
            print("Product ID 175 exists in the BST")
        else:
            print("Product ID 175 does not exist in the BST")

    elif ch == 4:
        b.root = b.delete_node(b.root, 100)
        print("Product ID 100 deleted successfully")

    elif ch == 5:
        print("Inorder Traversal:")
        b.inorder(b.root)
        print()

        print("Preorder Traversal:")
        b.preorder(b.root)
        print()

        print("Postorder Traversal:")
        b.postorder(b.root)
        print()

    elif ch == 6:
        print("Minimum Product ID:", b.minimum())
        print("Maximum Product ID:", b.maximum())

    elif ch == 7:
        print("Exiting program")
        break

    else:
        print("Invalid choice")