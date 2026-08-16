# Task 1 - To-Do List


A simple command-line To-Do List application built using Python as my first internship task at Decode Labs.


## What It Can Do


- Add multiple tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- View pending tasks
- View completed tasks
- View task summary
- Display tasks with numbers
- Handle invalid inputs
- Handle invalid task numbers
- Prevent marking an already completed task


## Python Concepts Used


- Lists
- `while` loop
- `for` loop
- `match-case`
- `if-else`
- `try-except`
- `enumerate()`
- `break`
- `append()`
- `pop()`
- `len()`
- f-strings


## How It Works


The application provides a menu where the user can choose an operation.

    ========= TO-DO LIST =========
    1. Add Task
    2. Update Task
    3. Delete Task
    4. Mark Task as Completed
    5. View Pending Tasks
    6. View Completed Tasks
    7. Task Summary
    8. Exit
    ==============================


### Add Task

The user can add tasks to the To-Do List.

    Enter your choice (1-8): 1

    Enter the number of tasks you want to add: 2
    Enter task 1: Learn Python
    Enter task 2: Practice Coding

    Task added successfully!

    Current Task List:
    1. Learn Python
    2. Practice Coding


### Update Task

The user can select a task number and update the task.

    Enter your choice (1-8): 2

    Enter the task number to update: 1
    Enter the new task: Learn Python Basics

    Task updated successfully!

    Updated Task List:
    1. Learn Python Basics
    2. Practice Coding


### Delete Task

The user can select a task number and remove it from the list.

    Enter your choice (1-8): 3

    Enter the task number to delete: 2

    Task 'Practice Coding' deleted successfully!


### Mark Task as Completed

The user can mark a task as completed using `[✅]`.

    Enter your choice (1-8): 4

    Enter the task number to mark as completed: 1

    Task 'Learn Python Basics' marked as completed!

    1. Learn Python Basics [✅]


### View Pending Tasks

Displays only tasks that are not completed.

    Enter your choice (1-8): 5

    Pending Tasks:
    2. Practice Coding


### View Completed Tasks

Displays only tasks marked as completed.

    Enter your choice (1-8): 6

    Completed Tasks:
    1. Learn Python Basics [✅]


### Task Summary

Displays the total, completed, and pending task count.

    Enter your choice (1-8): 7

    Total Tasks: 2
    Completed Tasks: 1
    Pending Tasks: 1


### Exit

Closes the To-Do List application.

    Enter your choice (1-8): 8

    Exiting To-Do List...


## Completed Task Indicator


Completed tasks are marked using:

    [✅]


This makes it easy to identify completed and pending tasks.


## Task Summary


The application keeps track of:

    Total Tasks
    Completed Tasks
    Pending Tasks


## How to Run


Make sure Python is installed, then run:

    python task1.py


## Task Details


Internship: Decode Labs  
Task: Task 1 - To-Do List Application  
Language: Python  
Type: Command-Line Application  
Status: Completed


## Author


Kaviyaa Padmavathi


# Task 2 - Expense Tracker


A simple command-line Expense Tracker built using Python as my second internship task at Decode Labs.


## What It Can Do


- Enter multiple expenses
- Store expenses in a list
- Calculate total expenses automatically
- Display each expense with numbers
- Display expenses in Indian Rupees
- Generate a simple expense receipt
- Use `0` to finish entering expenses


## Python Concepts Used


- Lists
- `while` loop
- `for` loop
- `if` statement
- `break`
- `enumerate()`
- `append()`
- Accumulator
- `float()`
- f-strings


## How It Works


The application allows the user to enter expenses continuously.

The user can enter multiple expenses:

    Enter Expense: 100
    Enter Expense: 22
    Enter Expense: 19

When the user enters `0`, the program stops taking expenses and generates the receipt.

    Enter Expense: 0


## Expense Flow


    Enter Expense
          ↓
    Check Expense
          ↓
       Is it 0?
       /     \
     Yes      No
      ↓        ↓
     Stop   Store Expense
                ↓
           Add to Total
                ↓
          Enter Next Expense
                ↓
          Generate Receipt


## Sample Receipt


    ============RECIPT=============
    Expense 1 : ₹100.0
    Expense 2 : ₹22.0
    Expense 3 : ₹19.0
    --------------------------------
    Total expense is : ₹141.0
    ===============================


## Key Idea


The total expense is calculated using an accumulator.

    total += expense

Each expense is added to the previous total.

The expenses are stored in a list and displayed using `enumerate()`.


## Sample


    Welcome to Expense Tracker

    Enter 0 to exit

    Enter Expense: 100
    Enter Expense: 22
    Enter Expense: 19
    Enter Expense: 0

    ============RECIPT=============
    Expense 1 : ₹100.0
    Expense 2 : ₹22.0
    Expense 3 : ₹19.0
    --------------------------------
    Total expense is : ₹141.0
    ===============================


## How to Run


Make sure Python is installed, then run:

    python task2.py


## Task Details


Internship: Decode Labs  
Task: Task 2 - Expense Tracker  
Language: Python  
Type: Command-Line Application  
Status: Completed


## Author


Kaviyaa Padmavathi
