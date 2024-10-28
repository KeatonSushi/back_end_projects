tasks = []

def show_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added task: '{task}'")

def delete_task():
    if not tasks:
        print("There are no tasks.")
        main()
    else:
        try:
            show_tasks()
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Deleted task: '{removed_task}'")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def erase_all_tasks():
    confirmation = input("Are you sure you want to delete all tasks? (y/n): ").lower()
    if confirmation == 'y':
        tasks.clear()
        print("All tasks have been erased.")
    elif confirmation == 'n':
        print("Erase all tasks canceled.")
        main()
    else:
        print("Incorrect choice. Try again.")
        erase_all_tasks()

def main():
    while True:
        print("\nTo-Do List Options:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Erase all tasks")
        print("5. Quit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            erase_all_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()