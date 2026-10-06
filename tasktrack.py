"""A command-line task manager created for CPS 310.
Author: Kalob Smith
Course: CPS 310
"""

TASKS_FILE = "tasks.txt"


def display_menu():
    """Display the available TaskTrack menu options."""
    print("\nTaskTrack Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove a task")
    print("4. Exit")


def add_task(tasks):
    """Prompt the user for a task and add it to the task list."""

    task = input("Enter a new task: ").strip()

    # check if input empty
    if not task:
        print("A task cannot be empty.")
    else:
        tasks.append(task)
        print(f"new task '{task}' added successfully.")


def view_tasks(tasks):
    """Display all tasks currently stored in the task list."""

    if not tasks:
        print("No tasks found")
    else:
        print("\nTasks:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


def load_tasks(filename):
    """Load tasks from a text file and return them as a list."""

    tasks = []

    try:
        with open(filename, "r") as file:
            for line in file:
                if not line.strip():
                    continue

                else:
                    task = line.strip()
                    tasks.append(task)

    except FileNotFoundError:
        # A new project may not have a task file yet.
        return []

    return tasks


def save_tasks(tasks, filename):
    """Save all tasks to a text file."""

    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")


def remove_task_by_number(tasks, task_number):
    """Remove a task by its displayed number and return the removed task.
    
    Return None when the task number is outside the valid range.
    """

    # if task_number is less than or equal to 0, or larger than len(tasks), return None
    if task_number <= 0 or task_number > len(tasks):
        return None
    
    else:
        return tasks.pop(task_number - 1)




def remove_task(tasks):
    """Prompt the user to select and remove a task.

    Return True when a task is removed and False otherwise.
    """
    
    if not tasks:
        print("no tasks are available to remove.")
        return False

    view_tasks(tasks)

    # input, and data type check
    while True:
        try:
            selection = int(
                input(
                    "Enter the number of the task to remove, or " 
                    "type '-1' to exit to menu: "
                ).strip()
            )

        except ValueError:
            print("Please enter a valid number/integer.")
            continue

        else:
            if selection == -1:
                print("Returning to menu.")
                return False
            
            else:
                # if integer input, and not returning to menu:
                removed_task = remove_task_by_number(tasks, selection)

                if removed_task is None:
                    print("Invalid selection")
                    continue

                else:
                    print(f"Task: {removed_task} has been removed.")
                    break

    return True


def main():
    """Run the TaskTrack menu until the user chooses to exit."""

    tasks = load_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks, TASKS_FILE)

        elif choice == "3":
            if remove_task(tasks):  # if changes are made
                save_tasks(tasks, TASKS_FILE)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()