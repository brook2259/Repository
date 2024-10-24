def main():
    class Student:
        all_students = []  # Class-level attribute to store all students

        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.subjects = {}  # Initialize with an empty dictionary for subjects and grades
            Student.all_students.append(self)

        @classmethod
        def get_all_students(cls):
            return cls.all_students

        @classmethod
        def find_student(cls, name):
            for student in cls.all_students:
                if student.name == name:
                    return student
            return None

        def add_subject_and_grade(self, subject, grade):
            self.subjects[subject] = grade

    def add_student():
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        new_student = Student(name, age)
        print(f"Added {name} to the list.")
    
    def add_subjects_to_student():
        name = input("Enter the name of the student to add subjects to: ")
        student = Student.find_student(name)
        if student:
            num_entries = int(input(f"How many subjects would you like to add for {student.name}? "))
            for _ in range(num_entries):
                subject = input("Enter subject: ")
                grade = int(input("Enter grade: "))
                student.add_subject_and_grade(subject, grade)
            print(f"Updated subjects for {student.name}: {student.subjects}")
        else:
            print(f"Student named {name} not found.")
    
    def student_average():
        name = input("Enter the name of the student to calculate the average for: ")
        student = Student.find_student(name)
        if student and student.subjects:
            grades = student.subjects.values()
            stu_avg = sum(grades) / len(grades)  # Calculate the average
            print(f'The student\'s average is: {stu_avg}')
        else:
            print('There are no grades to calculate.')

    while True:
        action = input("Would you like to (1) add a new student, (2) add subjects to an existing student, or (3) calculate student average? (Enter 1, 2, or 3): ")
        if action == '1':
            add_student()
        elif action == '2':
            add_subjects_to_student()
        elif action == '3':
            student_average()
        else:
            break

    # Display all students
    for student in Student.get_all_students():
        print(f"Student: {student.name}, Age: {student.age}, Subjects: {student.subjects}")

# Call the main function
main()
