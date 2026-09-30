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
        
    return


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

def remove_task(tasks):
    """Prompt the user to select and remove a task.
        Return True when a task is removed and False otherwise.
        """
    if not tasks:
        print("no tasks are available to remove.")
        return False

    view_tasks(tasks)

    # input, and data type check   
    while(True):
        try:
            selection = int(input("Enter the number of the task to remove, or " 
            "type '-1' to exit to menu: ").strip())
        except ValueError:
            print("Please enter a valid number/integer.")
            selection = 0
        else:
            # if user types -1
            if selection == -1:
                print("Returning to menu.")
                return(False)
            # if user types any int not in tasks[]
            elif selection < 1 or selection > len(tasks):
                print("No task with that number found.")
                continue
            # if user types any int in tasks[]
            else:
                remove_conf = tasks[selection - 1] # for confirmation mesg.
                print(f"Removing task {selection}, {remove_conf}...")
                tasks.pop(selection - 1)
                print(f"Removed: {remove_conf}, from tasks list.")
                break
    return True

def main():
    """Run the TaskTrack menu until the user chooses to exit."""
    tasks = load_tasks(TASKS_FILE)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks, TASKS_FILE)
        elif choice == "3":
            if remove_task(tasks): # if changes are made
                save_tasks(tasks, TASKS_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()