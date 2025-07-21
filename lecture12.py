import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks.values()) / len(self.marks)

    def display_info(self):
        self.greet()
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Average: {self.calculate_average():.2f}")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }

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

    def save_students_to_json(self):
        with open("students.json", "w") as file:
            json.dump([student.to_dict() for student in self.students], file, indent=4)
        print("\nAll student details saved to 'students.json'.")

    def load_students_from_json(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)
                self.students = [Student(item["name"], item["age"], item["marks"]) for item in data]
            print("\nLoaded students from 'students.json' successfully.")
        except FileNotFoundError:
            print("\nNo existing data found. Starting fresh.")

    def update_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                print(f"Updating marks for {student.name}.")
                for subject in student.marks.keys():
                    new_mark = float(input(f"Enter new marks for {subject}: "))
                    student.marks[subject] = new_mark
                print(f"{student.name}'s marks updated successfully.")
                return
        print("Student not found.")

    def delete_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print(f"{student.name} has been removed from the records.")
                return
        print("Student not found.")

# Main control
manager = StudentManager()
manager.load_students_from_json()

while True:
    print("\n--- Student Manager Menu ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Name: ")
        age = int(input("Age: "))
        marks = {}
        for subject in ["English", "Math", "Science"]:
            mark = float(input(f"Enter marks for {subject}: "))
            marks[subject] = mark
        student = Student(name, age, marks)
        manager.add_student(student)

    elif choice == '2':
        manager.display_all_students()

    elif choice == '3':
        name = input("Enter the student's name to update: ")
        manager.update_student(name)

    elif choice == '4':
        name = input("Enter the student's name to delete: ")
        manager.delete_student(name)

    elif choice == '5':
        manager.save_students_to_json()
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")