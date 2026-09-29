import json
import os

FILE_NAME = "tasks.json"


# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Display all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n--- TO-DO LIST ---")

    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['description']} - {status}")


# Add a new task
def add_task(tasks):
    description = input("\nEnter task description: ")

    task = {
        "description": description,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


# Mark a task as done
def complete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to mark as done: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Delete a task
def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed['description']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():
    tasks = load_tasks()

    while True:
        print("\n====================")
        print("     TO-DO LIST")
        print("====================")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()