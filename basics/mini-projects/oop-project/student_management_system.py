# student_management_system.py
# Simple Student Management System using OOP

class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department

    def display_info(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("------------------------")


students = []

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        dept = input("Enter Department: ")

        student = Student(sid, name, dept)
        students.append(student)

        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                student.display_info()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")

  # Added OOP project: Student Management System
