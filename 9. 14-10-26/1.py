#creation of singly circular linked list

class Node:
    def __init__(self, val):
        self.data=val 
        self.next=None
class LinkedList:
    def __init__(self):
            self.head=None
    def append(self, new_node):
        if (self.head==None): #linklist in constructor
             self.head=new_node
             new_node.next=self.head #new
        else:
             temp=self.head
             while(temp.next != self.head):
                  temp=temp.next
             temp.next=new_node #appending new node
             new_node.next=self.head #new
    def print(self):
        print()
        print("list elements: ")
        temp=self.head
        while(True):
              print(temp.data, end = " ")
              temp=temp.next
              if temp == self.head:
                   break


list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.print()