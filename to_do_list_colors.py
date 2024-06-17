red_color = '\033[1;36;41m'
green_color = '\033[1;36;42m'
default_color =  '\033[m'
tasks = []

while True:
    print(f'\n{green_color}====== Welcome to your To Do List ======{default_color}\n')
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
            print(f'{green_color}Task added!{default_color}\n')
            
    elif choice == '2':
        print('Tasks: ')
        for index, task in enumerate(tasks):
            print(f'{index+1}.{task}')
        
    elif choice == '3':
        task_to_mark_done = int(input('Type which task do you want to mark as done: '))
        
        if task_to_mark_done > 0 and task_to_mark_done <= len(tasks):
            tasks[task_to_mark_done-1] = tasks[task_to_mark_done-1].replace('Not done', 'Done')
            print(f'\n{green_color}Tasked marked as done!{default_color}')
    
    elif choice == '4':
        print(f'{green_color}Thanks for use our To do List{default_color}\n')
        break
    
    else:
        print(f'{red_color}Invalid choice. Type a valid option.{default_color}')
