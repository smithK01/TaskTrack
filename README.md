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
- tasks.txt - [The data file that stores tasks on each new line]
- .gitignore - [The information that Git uses to manage the repository]

## Running the Program

open command terminal
navigate to directory containing tasktrack.py and tasks.txt
run tasktrack.py
enter desired menu number to either view, or add tasks to the task list.

Ex:

cmd.exe
cd C:/Users/%yourusernamehere%/documents
python tasktrack.py

## How task persistence works

tasks are taken from user input, stripped, and written to tasks.txt. When writing new tasks to an already populated tasks.txt file, add_tasks() skips any lines in the file that are already populated.


## Sample Interaction

TaskTrack Menu
1. View tasks
2. Add task
3. Exit
Choose an option: 1

Tasks:
1. complete ICA04
2. Review GitHub commands
3. Update the TaskTrack README
4. test persistent storage
5. Push tasktrack.py to GitHub

TaskTrack Menu
1. View tasks
2. Add task
3. Exit
Choose an option: 2
Enter a new task: I'm adding a new task!
new task 'I'm adding a new task!' added successfully.

TaskTrack Menu
1. View tasks
2. Add task
3. Exit
Choose an option: 1

Tasks:
1. complete ICA04
2. Review GitHub commands
3. Update the TaskTrack README
4. test persistent storage
5. Push tasktrack.py to GitHub
6. I'm adding a new task!

TaskTrack Menu
1. View tasks
2. Add task
3. Exit
Choose an option: 3
Goodbye!


## Current Limitation

unable to remove tasks without manually doing so from the tasks.txt file.