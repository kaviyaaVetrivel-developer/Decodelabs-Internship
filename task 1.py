to_do_list=[]

while True:
    print("\n========= TO-DO LIST =========")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. View Pending Tasks")
    print("6. View Completed Tasks")
    print("7. Task Summary")
    print("8. Exit")
    print("==============================")
    try:
        choice = int(input("\nEnter your choice (1-8): "))

        match choice:
            case 1:
                count=int(input("\nEnter the number of tasks you want to add: "))
                for i in range(count):
                    task = input(f"Enter task {i + 1}: ")
                    to_do_list.append(task)
                print("Task added successfully!")
                print("Current Task List:")
                for i, task in enumerate(to_do_list, start=1):
                    print(f"{i}. {task}")

            case 2:
                task_index = int(input("\nEnter the task number to update:"))
                new_task = input("Enter the new task: ")
                to_do_list[task_index - 1] = new_task
                print("Task updated successfully!")
                print("Updated Task List:")
                for i, task in enumerate(to_do_list, start=1):
                    print(f"{i}. {task}")

            case 3:
                task_index = int(input("\nEnter the task number to delete:"))
                deleted_task = to_do_list.pop(task_index - 1)
                print(f"Task '{deleted_task}' deleted successfully!")
                print("Updated Task List:")
                for i, task in enumerate(to_do_list, start=1):
                    print(f"{i}. {task}")

            case 4:
                task_index = int(input("\nEnter the task number to mark as completed:"))
                completed_task = to_do_list[task_index - 1]

                if "[✅]" in completed_task:
                    print("Task is already completed!")
                else:
                    to_do_list[task_index - 1] = f"{completed_task} [✅]"
                    print(f"Task '{completed_task}' marked as completed!")

                for i , task in enumerate(to_do_list, start=1):
                    print(f"{i}. {task}")

            case 5:
                print("\nPending Tasks:")
                for i, task in enumerate(to_do_list, start=1):
                    if "[✅]" not in task:
                        print(f"{i}. {task}")
            case 6:
                print("\nCompleted Tasks:")
                for i, task in enumerate(to_do_list, start=1):
                    if "[✅]" in task:
                        print(f"{i}. {task}")

            case 7:
                total_tasks = len(to_do_list)
                completed_tasks = 0
                print(f"\nTotal Tasks: {total_tasks}")

                for task in to_do_list:
                    if "[✅]" in task:
                        completed_tasks += 1
                print(f"Completed Tasks: {completed_tasks}")

                pending_tasks = total_tasks - completed_tasks
                print(f"Pending Tasks: {pending_tasks}")

            case 8:
                print("Exiting To-Do List...")
                break 

            case _:
                print("Invalid choice! Please enter a number between 1 and 8.")
                
    except ValueError:
        print("\nPlease enter a valid number.")

    except IndexError:
        print("\nInvalid task number. Please enter a task number that exists.")
