#practical assessment 

#Ass1: Create a Singly Linear Linked List with following operations

#Create Linked List
#Traverse and print the node values
#Insert node at a specific position
#Find Middle node and print its value
#Delete node
#Reverse list
#Calculate the sum of every two consecutive node values.
#Constraints:
#Time limit: 2000 ms
#Memory limit: 256 MB

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create Linked List
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    # Traverse and print node values
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Insert node at a specific position (0-based)
    def insert(self, val, pos):
        new_node = Node(val)

        if pos < 0:
            print("Invalid position")
            return

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        i = 0

        while temp != None and i < pos - 1:
            temp = temp.next
            i += 1

        if temp == None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Find middle node
    def find_middle(self):
        slow = self.head
        fast = self.head

        if self.head == None:
            print("List is empty")
            return

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # Delete node by value
    def delete(self, val):
        if self.head == None:
            print("List is empty")
            return

        if self.head.data == val:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next != None:
            if temp.next.data == val:
                temp.next = temp.next.next
                return
            temp = temp.next

        print("Value not found")

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Sum every two consecutive node values
    def sum_consecutive(self):
        temp = self.head

        while temp != None and temp.next != None:
            print(temp.data + temp.next.data)
            temp = temp.next


# Main program
ll = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

ll.append(n1)
ll.append(n2)
ll.append(n3)
ll.append(Node(40))

print("Original Linked List:")
ll.print_list()

print("Insert 15 at position 1:")
ll.insert(15, 1)
ll.print_list()

print("Middle node:")
ll.find_middle()

print("Delete node with value 20:")
ll.delete(20)
ll.print_list()

print("Reverse Linked List:")
ll.reverse()
ll.print_list()

print("Sum of consecutive node values:")
ll.sum_consecutive()
