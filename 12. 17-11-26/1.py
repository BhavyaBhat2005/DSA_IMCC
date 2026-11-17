#Q. 1 Hospital Emergency Management  
#Develop a Python program to manage patients in a hospital using a Priority Queue 
#Requirements: 
#1. Accept patient ID, patient name and priority 
#2. Priority 1 represents Critical, 2 represents Serious and 3 represents Normal 
#3. Patients with higher priority must be treated first 
#Write following functions 
#1. Add Patient (enqueue) 
#2. Display the next patient to be treated. (display_next) 
#3. Remove a patient from the queue after treatment. (dequeue) 
#4. Display all waiting patients in priority order(display_all)

class Node: #creating class Node 
    def __init__(self, pid, pname, priority): #creating constructor to store patient details 
        self.pid = pid
        self.pname = pname
        self.priority = priority 
        self.next = None #stores connection to next node 

class Hospital:
    def __init__(self):
        self.front=None #variable for first patient in queue 

#1. Accept patient ID, patient name and priority 

    def enqueue(self, pid, pname, priority):
        new_node = Node(pid, pname, priority)

        if self.front == None:
            self.front = new_node 

        elif priority < self.front.priority:
            new_node.next = self.front  #connects new node to existing node 
            self.front = new_node #changes front pointer to new node 

        else: #if queue is not empty and new patient does not have higher oriority over first patient 
            temp = self.front 

            while temp.next != None and temp.next.priority <= priority:
                temp = temp.next 

            new_node.next = temp.next #new node connects to node after temp 
            temp.next = new_node #connects current node to new node 

#2. Display the next patient to be treated. (display_next) 

    def display_next(self):
        if self.front == None: #checks if queue is empty 
            print("No patients waiting")
        else:
            print("next patient to be treated:")
            print("Patient ID:", self.front.pid)
            print("Patient Name:", self.front.pname)
            print("Priority:", self.front.priority)

#3. Remove a patient from the queue after treatment. (dequeue) 

    def dequeue(self): #function to remove element from queue 
        if self.front == None:
            print("Queue is empty")
        else:
             print("Patient treated", self.front.pname)
             self.front = self.front.next #moves the front pointer to nexr patitent 


#4. Display all waiting patients in priority order(display_all)

    def display_all(self):
        if self.front == None:
            print("no patients waiting")
        else:
            temp = self.front
            
            while temp != None:
                print("Patient ID:", temp.pid)
                print("Patient Name:", temp.pname)
                print("Priority:", temp.priority)
                temp = temp.next
    
    
h = Hospital() #creating hospital object 

while True:
    print("\n Hospital Emergency Management")
    print("1. Add patient")
    print("2. Display next patient")
    print("3. Remove patient")
    print("4. Display all patient")
    print("5. Exit")

    choice = int(input("Enter your choice"))
    
    if choice == 1: #checks if user has added patient 
        pid = int(input("Enter Patient ID: "))
        pname = input("Enter Patient Name: ")

        print("1. Critical  2. Serious  3. Normal")
        priority = int(input("Enter Priority: "))

        if priority >= 1 and priority <= 3:
            h.enqueue(pid, pname, priority)
        else:
            print("Invalid priority!")

    elif choice == 2:
        h.display_next()

    elif choice == 3:
        h.dequeue()

    elif choice == 4:
        h.display_all()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
