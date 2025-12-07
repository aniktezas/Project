
tasks=[]

while True:
    print('''What do you want to do?
1. Add a new task
2. View all tasks
3. Mark a task as completed
4. Exit''')
    
    k=int(input())
    

    if k==1:
        p=int(input('How many tasks do you want to add? \n'))
        for i in range(p):
            tasks.append(input('Enter task: \n'))
            print('Tasks added successfully')
    elif k==2:
        print('Your tasks are:\n')
        for task in tasks:
            print(task)
    elif k==3:
        ttc=int(input('Enter the task number to mark as completed: \n'))
        if 0 < ttc <= len(tasks):
            a=tasks.pop(ttc-1)
            print(f'Task "{a}" marked as completed and removed from the list.')
    elif k==4:
        print('''Exiting the to-do list application.
Thank you for using it!''')
        break
    else:
        print('Invalid option. Please try again.')      
