"""

Simple Task Manager
-------------------
A beginner friendly command-line app that allows users to:
- View tasks
- Add new tasks
- Complete tasks
- Delete tasks
- Edit existing tasks
The tasks are saved to a file for persistence.

Built by Althani Ching, using basic Python concepts like:
- Lists
- Functions
- File I/O
- Error handling

"""


FILENAME = "tasks.txt"

# Load task from file or return empty list
def load_tasks():
    try: 
        with open(FILENAME, "r") as file:
            return[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return[]

# Save the current list of task to the file 
def save_tasks(tasks):
    with open(FILENAME, "w") as file:   
        for task in tasks:
            file.write(task + "\n")

tasks = load_tasks()

# Display or show the menu options
def show_menu():
    print("\n=== Task Manager====")  
    print("1. View Tasks")             
    print("2. Add Task")               
    print("3. Complete Task")          
    print("4. Delete Task")            
    print("5. Edit Task")              
    print("6. Quit")                   

# Main program loop 
while True:

    show_menu()
    choice = int(input("\nChoose an option (1-6): "))

    # Option 1: View Tasks
    if choice == 1:
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks found. Your list is empty.\n")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        

    # Option 2: Add Task
    elif choice == 2:
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added!")


    # Option 3: Complete Task
    elif choice == 3:
        try:                                
            task_num = int(input("Enter task number to complete: "))
            if 1 <= task_num <= len(tasks):
                completed = tasks.pop(task_num - 1) 
                save_tasks(tasks)                      
                print(f"Task {completed} completed!")
            else:
                print("Invalid task number.")
        except ValueError:
             print("Please enter a valid number.")


    # Option 4: Delete Task
    elif choice == 4:
        try: 
            task_num = int(input("Enter task to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted = tasks.pop(task_num - 1)
                save_tasks(tasks)           
                print(f"Task {deleted} deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

            
    # Option 5: Edit Task 
    elif choice == 5:
        try:
            task_num = int(input("Enter task to edit: "))
            if 1 <= task_num <= len(tasks):
                new_name = input("Enter the new task name: ")
                tasks[task_num - 1] = new_name
                save_tasks(tasks)
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError: 
            print("Please enter a valid number.")
            

    # Option 6: Quit
    elif choice == 6:
        print("Goodbye!")
        break
        
    # Prompt when the user choice a number that is not in the show menu.     
    else:
        print("Invalid choice. Please try again.")
    
