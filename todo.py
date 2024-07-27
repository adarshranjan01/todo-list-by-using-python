import os

def load_tasks(filename="tasks.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task, tasks):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(index, tasks):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task index")

def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task description: ")
            add_task(task, tasks)
            save_tasks(tasks)
        elif choice == '3':
            list_tasks(tasks)
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index, tasks)
                save_tasks(tasks)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
