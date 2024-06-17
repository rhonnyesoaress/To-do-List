tasks = []

while True:
    print(f'\n====== Welcome to your To Do List ======\n')
    print('1. Add new tasks')
    print('2. Show tasks')
    print('3. Mark Task as Done')
    print('4. Exit\n')

    choice = input('Choose an option: ')
    print('')
    
    if choice == '1':
        n_tasks = int(input('Type how many tasks do you want to add: '))
        
        for i in range(n_tasks):
            task = input('Type your task: ')
            task = task + ' - Not done'
            tasks.append(task)
            print(f'Task added!\n')
            
    elif choice == '2':
        print('Tasks: ')
        for index, task in enumerate(tasks):
            print(f'{index+1}.{task}')
        
    elif choice == '3':
        task_to_mark_done = int(input('Type which task do you want to mark as done: '))
        
        if task_to_mark_done > 0 and task_to_mark_done <= len(tasks):
            tasks[task_to_mark_done-1] = tasks[task_to_mark_done-1].replace('Not done', 'Done')
            print(f'\nTasked marked as done!')
    
    elif choice == '4':
        print(f'Thanks for use our To do List\n')
        break
    
    else:
        print(f'Invalid choice. Type a valid option.')