#in this app will be possible crud of task
import os

print('*-----------------------------*')
print('*Welcome to Made Your Task MYT*')
print('*-----------------------------*')
tasks = []

while True:
    print('--------------------------------------------------------')
    option = input('| With TASK: (a)DD|(s)HOW|(d)ELETE|(c)LEAR CMD|(e)XIT.: ')
    print('--------------------------------------------------------')
    
    if option == 'a':
        for task in tasks: 
            print(f'{tasks.index(task)+1} - {task}')
        
        task = input('\nType your task.: ')
        if task != '':
            print('\n')
            tasks.append(task)
        else:
            print('\n')
            print('do you need type anything! Try again')    
            print('\n')

    elif option == 's':
        if len(tasks) == 0:
            print('\nlist empty!\n')
        else:    
            for task in tasks: 
                print(f'{tasks.index(task)+1} - {task}')

    elif option == 'd':
        task_todelete = int(input('\ntype code of the task for delete.: '))
        task_todelete = task_todelete - 1;
        print('\n')
        try:
            tasks.pop(task_todelete)
        except:
            print('Task does not exist\n')

    elif option == 'e':
        break
    
    elif option == 'c':
        os.system('cls') or None
    else:
        print('\ninvalid option!\n')

print('\nThank for used my app by Sautier Alexsander\n')
input('')        