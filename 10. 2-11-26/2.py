#Q2Write a program to perform the following operations on a Linear Queue 
#1. Enqueue an element into the queue  
##2. Dequeue an element from the queue  
#3. Display 
#4. Reverse the queue using stack 
#5.  Merge two queues into one. 
#6. Check if two queues are identical 



# Program to perform Linear Queue operations

# Create two empty queues
queue = []
queue2 = []

# Function to insert an element into the queue
def enqueue():
    element = input("Enter element to insert: ")

    # Insert the element at the rear
    queue.append(element)
    print("Element inserted successfully")

# Function to delete an element from the queue
def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        # Remove the frontmost element
        element = queue.pop(0)
        print("Deleted element:", element)

# Function to display the queue
def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue (front to rear):", queue)

# Function to reverse the queue using a stack
def reverse_queue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        stack = []

        # Remove queue elements and push them onto a stack
        while len(queue) > 0:
            stack.append(queue.pop(0))

        # Pop stack elements and insert them into the queue
        while len(stack) > 0:
            queue.append(stack.pop())

        print("Queue reversed successfully")
        print("Reversed queue:", queue)

# Function to enter elements into the second queue
def create_second_queue():
    queue2.clear()

    n = int(input("Enter number of elements in second queue: "))

    # Insert elements into the second queue
    for i in range(n):
        element = input("Enter element: ")
        queue2.append(element)

    print("Second queue:", queue2)

# Function to merge two queues
def merge_queues():
    # Create a new queue containing both queues
    merged = queue + queue2

    print("Merged queue:", merged)

# Function to check whether two queues are identical
def identical_queues():
    if queue == queue2:
        print("Both queues are identical")
    else:
        print("Queues are not identical")

# Main menu
while True:
    print("\n--- LINEAR QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse Queue using Stack")
    print("5. Merge Two Queues")
    print("6. Check Identical Queues")
    print("7. Create Second Queue")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enqueue()
    elif choice == "2":
        dequeue()
    elif choice == "3":
        display()
    elif choice == "4":
        reverse_queue()
    elif choice == "5":
        merge_queues()
    elif choice == "6":
        identical_queues()
    elif choice == "7":
        create_second_queue()
    elif choice == "8":
        print("Program terminated")
        break
    else:
        print("Invalid choice")