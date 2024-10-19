# Function to get tasks from the user
def tasks():
    task_list = []  # Initialize an empty list to store tasks

    # Prompt the user for multiple tasks
    while True:
        new_task = input('Add a task to the list (or type "done" to finish): ')
        if new_task.lower() == 'done':  # Check for exit condition
            break
        task_list.append(new_task)  # Append the user input to the list

    if len(task_list) > 3:  # Check if the number of tasks exceeds 3
        print('You have enough tasks for now.')
    else:
        print('You can add more tasks.')
    
    return task_list  # Return the list of tasks


# Function to remove a task from the list
def rem_tasks(task_list):
    rem = input('What task would you like to remove? ')
    if rem in task_list:
        task_list.remove(rem)  # Remove the task from the list
        print(f'Task "{rem}" removed.')
    else:
        print('Task not found.')
    return task_list


# Function to view current tasks
def view_tasks(task_list):
    print('Your current tasks:')
    for task in task_list:
        print(f'- {task}')
    return task_list


# Function to save the task list to a file
def save_tasks(task_list):
    task_file = 'tasks.txt'
    with open(task_file, 'w') as file:  # Open in 'w' mode to overwrite the file
        for items in task_list:
            file.write(f'{items}\n')  # Write each task on a new line
    print(f'Tasks saved to {task_file}')
    return task_file


# Main function to manage the tasks
def main():
    print('Let\'s add some tasks!')
    task_list = tasks()  # Get tasks from the user
    
    # Save the tasks
    save_tasks(task_list)

    # Ask if the user wants to remove an item
    while True:
        less_item = input('Would you like to remove an item? (y/n): ')
        if less_item.lower() in ['y', 'yes']:
            task_list = rem_tasks(task_list)  # Update the task list after removal
        else:
            break

    # View and save the final task list
    view_tasks(task_list)
    save_tasks(task_list)  # Save the tasks again after modification

# Run the main function
main()
