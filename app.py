#in this app will be possible crud of task
import os
from datetime import datetime

def main(option):
    if option == 'a':
        add_task()
    elif option == 's':
        show_task()
    elif option == 'd':
        delete_task()
    elif option == 'c':
        clear_cmd()
    elif option == 'e':
        exit_app()
    else:
        print('\ninvalid option!\n')

def add_task():
    task = input('\nType your task.: ')
    task = task + ' | Created: ' + datetime.strftime(datetime.now(), "%d/%m/%Y at %H:%M:%S")
    if task != '':
        tasks.append(task)
    else:
        print('\ndo you need type anything! Try again\n')    

def show_task():
    if len(tasks) == 0:
        print('\nlist empty!\n')
    else:    
        for task in tasks: 
            print(f'{tasks.index(task)+1} - {task}')

def delete_task():
    task_todelete = int(input('\ntype code of the task for delete.: '))
    task_todelete = task_todelete - 1;
    print('\n')
    try:
        tasks.pop(task_todelete)
    except:
        print('Task does not exist\n')

def clear_cmd():
    os.system('cls') or None

def exit_app():
    print('\nThank for used my app by Sautier Alexsander\n')         
    os._exit(0)

tasks = []

while True:
    option = input('''        Made Your Task MYT
        For create taks type     'a',
        For show taks type       's',
        For delete any taks type 'd',
        For clear cmd type       'c',
        For exit type            'e'
        option: ''')
   
    main(option)   
