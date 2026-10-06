# TaskTrack

A program that displays a menu to view and add tasks. Tasks are then saved to a file tasks.txt.

## Current Features

-Add tasks

-save tasks to tasks.txt file

-view tasks form tasks.txt file

## Version Control

This project uses Git to manage version control of the repository locally, and GitHub as it's remote repository.

Ex:

Commit code changes to the local repository,
Push accumulated commits from local repository to the online repository,
Pull changes from the online repository to the local repository.

## Requirements

-Python 3

## Project Files

- tasktrack.py - [The python file that displays the menu in the terminal, alowing the user to input and view tasks]
- test_tasktrack.py - [The python file that runs the tests for tasktrack.py]
- tasks.txt - [The data file that stores tasks on each new line]
- .gitignore - [Contains filenames that Git ignores and does not add to the local/online repository]
- REFLECTION.md - [The required reflection for ICA04, describing ## 1. Local and Remote Repositories, Connecting and Pushing, Cloning, Fetching and Pulling, and Focused Commits]


## Running the Program

open command terminal
navigate to directory containing tasktrack.py and tasks.txt
run tasktrack.py
enter desired menu number to either view, add, or remove tasks from the task list.

Ex:

cmd.exe
cd C:/Users/%yourusernamehere%/documents
python tasktrack.py


## Testing the Program

TaskTrack uses pytest to test logic. The tests are located in test_tasktrack.py and currently only verifies return values and task lists for the remove_task_by_number() function.

### Setting up the testing environment

open command terminal inside the TaskTrack project folder
run python -m venv .venv
run .\.venv\Scripts\Activate.ps1
run python -m pip install pytest

### Running the tests

when inside of the virtual environment (ie: the terminal is headed by (.venv))
run python -m pytest -v

if you open a new terminal, or otherwise are not in the virtual environment
run .\.venv\Scripts\Activate.ps1
to return to the virtual environment. Then you can resume testing.

### Current Tests

- removing the first task
- removing a middle task
- removing the last task
- reject input 0
- reject input > task list length
- removing from an empty list

    valid selections should remove and return said task. Invalid selections return None and do not change the task list.

    All six current tasks should pass.


## How task persistence works

tasks are taken from user input, stripped, and written to tasks.txt. When writing new tasks to an already populated tasks.txt file, add_tasks() skips any lines in the file that are already populated.


## Sample Interaction

TaskTrack Menu
1. View tasks
2. Add task
3. Remove a task
4. Exit
Choose an option: 1

Tasks:
1. complete ICA05
2. create an issue for tasktrack repo
3. create a pull request for tasktrack repo

TaskTrack Menu
1. View tasks
2. Add task
3. Remove a task
4. Exit
Choose an option: 2
Enter a new task: this is a task!
new task 'this is a task!' added successfully.

TaskTrack Menu
1. View tasks
2. Add task
3. Remove a task
4. Exit
Choose an option: 3

Tasks:
1. complete ICA05
2. create an issue for tasktrack repo
3. create a pull request for tasktrack repo
4. this is a task!
Enter the number of the task to remove, or type '-1' to exit to menu: 4
Task: this is a task! has been removed.

TaskTrack Menu
1. View tasks
2. Add task
3. Remove a task
4. Exit
Choose an option: 4
Goodbye!


## Current Limitations

None known currently