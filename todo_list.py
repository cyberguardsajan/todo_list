

def main():
    filename = "tasks.txt"

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(filename, task)
            print("Task added successfully.")
        elif choice == '2':
            view_tasks(filename)
        elif choice == '3':
            view_tasks(filename)
            task_number = int(input("Enter task number to mark as completed: "))
            if mark_task_completed(filename, task_number):
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        elif choice == '4':
            view_tasks(filename)
            task_number = int(input("Enter task number to delete: "))
            if delete_task(filename, task_number):
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        elif choice == '5':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice, please try again.")


def add_task(filename, task):
    with open(filename, 'a') as file:
        file.write(f"{task}\n")

def view_tasks(filename):
    with open(filename, 'r') as file:
        tasks = file.readlines()
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")







def mark_task_completed(filename, task_number):
    with open(filename, 'r') as file:
        tasks = file.readlines()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = f"{tasks[task_number - 1].strip()} - Completed\n"
        with open(filename, 'w') as file:
            file.writelines(tasks)
        return True
    else:
        return False





def delete_task(filename, task_number):
    with open(filename, 'r') as file:
        tasks = file.readlines()
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        with open(filename, 'w') as file:
            file.writelines(tasks)
        return True
    else:
        return False






if __name__ == "__main__":
    main()
