
user_dict = {}


num_entries = int(input('Enter the number of subjects and grades: '))


for i in range(num_entries):
    key = str(input('Enter subject (key): '))  
    value = int(input('Enter grade (value): '))  
    user_dict[key] = value  

print('Dictionary after adding user input: ', user_dict)

if user_dict: 
    average = sum(user_dict.values()) / len(user_dict)
    print(f'The average grade is: {average:.2f}')
else:
    print('No grades entered to calculate an average.')


grade_file = 'grades.txt'


with open(grade_file, 'w') as file:
    for key, value in user_dict.items():
        file.write(f"{key}: {value}\n")

print(f'Grades have been written to {grade_file}')