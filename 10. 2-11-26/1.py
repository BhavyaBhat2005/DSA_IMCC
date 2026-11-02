#Q. 1 Create a Stack with following operations 
#1. Push 
#2. Pop 
#3. Display 
#4. Reverse String using Stack 
#5. Reverse Stack using another Stack


# Program to perform Stack operations

# Create an empty stack
stack = []


# Function to push an element into the stack
def push():
    # Accept an element from the user
    element = input("Enter element to push: ")

    # Add the element to the top of the stack
    stack.append(element)

    print("Element pushed successfully")


# Function to pop an element from the stack
def pop():
    # Check whether the stack is empty
    if len(stack) == 0:
        print("Stack Underflow")

    else:
        # Remove and return the topmost element
        element = stack.pop()

        print("Popped element:", element)


# Function to display all elements of the stack
def display():
    # Check whether the stack is empty
    if len(stack) == 0:
        print("Stack is empty")

    else:
        # Display elements from bottom to top
        print("Stack (bottom to top):", stack)


# Function to reverse a string using a stack
def reverse_string():
    # Accept a string from the user
    string = input("Enter a string: ")

    # Create a temporary stack
    temp = []

    # Push each character of the string onto the stack
    for ch in string:
        temp.append(ch)

    # Pop characters to form the reversed string
    result = ""

    while len(temp) > 0:
        result = result + temp.pop()

    # Display the reversed string
    print("Reversed string:", result)

# Function to reverse the stack using another stack
def reverse_stack():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        temp = []

        # Move all elements from the original stack
        # to the temporary stack
        while len(stack) > 0:
            temp.append(stack.pop())

        # Copy elements back in reversed order
        while len(temp) > 0:
            stack.insert(0, temp.pop())

        print("Stack reversed successfully")
        print("Reversed stack:", stack)

# Main program: display the menu repeatedly
while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String using Stack")
    print("5. Reverse Stack using Another Stack")
    print("6. Exit")

    # Accept the user's menu choice
    choice = input("Enter your choice: ")

    # Call the function according to the selected choice
    if choice == "1":
        push()

    elif choice == "2":
        pop()

    elif choice == "3":
        display()

    elif choice == "4":
        reverse_string()

    elif choice == "5":
        reverse_stack()

    elif choice == "6":
        # Stop the loop and terminate the program
        print("Program terminated")
        break

    else:
        # Handle an invalid menu choice
        print("Invalid choice. Please try again.")
