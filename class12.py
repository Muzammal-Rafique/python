# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, I am {self.name}, {self.age} years old.")

# class Student(Person):
#     def __init__(self, name, age, english, math, science):
#         super().__init__(name, age)
#         self.english = english
#         self.math = math
#         self.science = science
#         self.average = self.calculate_average()

#     def calculate_average(self):
#         return (self.english + self.math + self.science) / 3

#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#         print(f"English: {self.english}, Math: {self.math}, Science: {self.science}")
#         print(f"Average: {self.average:.2f}")

# # Usage:
# student1 = Student("Muzamil", 19, 85, 90, 78)
# student1.greet()
# student1.display_info()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks  # marks is a dict: {subject: mark}

    def calculate_average(self):
        return sum(self.marks.values()) / len(self.marks)

    def display_info(self):
        self.greet()
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Average: {self.calculate_average():.2f}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"\nStudent {student.name} added successfully.")

    def display_all_students(self):
        print("\n--- All Students ---")
        if not self.students:
            print("No students to display.")
            return
        for student in self.students:
            student.display_info()
            print("-" * 20)

    def save_students(self):
        with open("students_inheritance.txt", "w") as file:
            for student in self.students:
                marks_str = ', '.join([f"{sub}: {mark}" for sub, mark in student.marks.items()])
                avg = student.calculate_average()
                file.write(f"Name: {student.name}, Age: {student.age}, Marks: {marks_str}, Average: {avg:.2f}\n")
        print("\nAll student details saved to 'students_inheritance.txt'.")

# Create the manager
manager = StudentManager()

# Add 2-3 students using dummy data
for i in range(3):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    marks = {}
    for subject in ["English", "Math", "Science"]:
        mark = float(input(f"Enter marks for {subject}: "))
        marks[subject] = mark

    student = Student(name, age, marks)
    manager.add_student(student)

# Display all students
manager.display_all_students()

# Save to file
manager.save_students()
