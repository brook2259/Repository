import os

directory = os.getcwd()

entry = input('Would you like to start a new diary entry? Y/N' )

if entry.lower() in ['y', 'yes']:
    
    new_file = input('What would you like to name the file? ')
    with open(new_file, 'w+') as file:
        file.write('Begin writing here')
    
elif entry.lower() in ['n', 'no']:
    
    old_file = input('What file would you like to open? ')
    
    full_path = os.path.join(directory, old_file)
    
    try:
        if os.path.isfile(full_path):
            with open(full_path, 'a+') as prev_file:
                prev_file.write('\nBegin writing here')
    
        else:
            print(f'The file "{old_file}" does not exist in the directory "{directory}".')
            
    except (FileNotFoundError, PermissionError) as e:
        print(f'There was an error: {e}')
        
else:
    print('Maybe tomorrow!')