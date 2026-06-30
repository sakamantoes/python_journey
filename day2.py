# Rule definitions
rule1Add = 1
rule2View = 2
rule3Complete = 3
rule4Delete = 4
rule5Exit = 5

todoStore = []

print("=" * 40)
print("      WELCOME TO YOUR TODO LIST")
print("=" * 40)

while True:
    # Display menu
    print("\nWhat would you like to do?")
    print(f"{rule1Add}. Add a task")
    print(f"{rule2View}. View all tasks")
    print(f"{rule3Complete}. Complete a task")
    print(f"{rule4Delete}. Delete a task")
    print(f"{rule5Exit}. Exit")
    print("-" * 40)
    
    # Get user choice
    choice = input("Enter your choice (1-5): ")
    
    # Add task
    if choice == str(rule1Add):
        task = input("Enter the task you want to add: ")
        if task.strip():  # Check if task is not empty
            todoStore.append(task)
            print(f" '{task}' has been added!")
        else:
            print(" Task cannot be empty!")
    
    # View all tasks
    elif choice == str(rule2View):
        if todoStore:
            print("\nYour Todo List:")
            print("-" * 30)
            for i, mark in enumerate(todoStore, 1):
                print(f"{i}. {mark}")
            print("-" * 30)
            print(f"Total tasks: {len(todoStore)}")
        else:
            print(" Your todo list is empty!")
    
    # Complete a task
    elif choice == str(rule3Complete):
        if todoStore:
            print("\nYour tasks:")
            for number, task in enumerate(todoStore, 1):
                print(f"{number}. {task}")
            task = input("\nEnter the task number or name to mark as complete: ")
            
            # Check if input is a number (task index)
            if task.isdigit():
                index = int(task) - 1
                if 0 <= index < len(todoStore):
                    completed_task = todoStore.pop(index)
                    print(f" '{completed_task}' has been marked as complete!")
                else:
                    print(" Invalid task number!")
            else:
                # Check by task name
                if task in todoStore:
                    todoStore.remove(task)
                    print(f" '{task}' has been marked as complete!")
                else:
                    print(" Task not found!")
        else:
            print(" No tasks to complete!")
    
    # Delete a task
    elif choice == str(rule4Delete):
        if todoStore:
            print("\nYour tasks:")
            for i, task in enumerate(todoStore, 1):
                print(f"{i}. {task}")
            task = input("\nEnter the task number or name to delete: ")
            
            if task.isdigit():
                index = int(task) - 1
                if 0 <= index < len(todoStore):
                    deleted_task = todoStore.pop(index)
                    print(f" '{deleted_task}' has been deleted!")
                else:
                    print(" Invalid task number!")
            else:
                if task in todoStore:
                    todoStore.remove(task)
                    print(f" '{task}' has been deleted!")
                else:
                    print(" Task not found!")
        else:
            print(" No tasks to delete!")
    
    # Exit
    elif choice == str(rule5Exit):
        print("\n Goodbye! Have a productive day!")
        break
    
    # Invalid choice
    else:
        print(" Invalid choice! Please enter a number between 1-5.")

print("\n" + "=" * 40)