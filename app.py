#in this app will be possible crud of task

print('Welcome to Made Your Task MYT')

tasks = []

while True:


    option = input('For (a)DD|(s)HOW|(d)ELETAR|(e)XIT.: ')
    
    if option == 'a':
        for task in tasks: 
            print(f'{tasks.index(task)+1} - {task}')

        task = input('Type your task.:')
        tasks.append(task)
    elif option == 's':
        if len(tasks) == 0:
            print('list empty!')
        else:    
            for task in tasks: 
                print(f'{tasks.index(task)+1} - {task}')
    elif option == 'd':
        task_todelete = int(input('type code of the task for delete.: '))
        tasks.pop(task_todelete-1)
    elif option == 'e':
        break
    else:
        print('invalid option!')

print('Thank for used my app by Sautier Alexsander')        