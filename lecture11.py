class Student:
    def __init__(self, name, english, math, science):
        self.name = name
        self.english = english
        self.math = math
        self.science = science
        self.average = (english + math + science) / 3

    def display_info(self):
        print(f"\nName: {self.name}")
        print(f"English: {self.english}")
        print(f"Math: {self.math}")
        print(f"Science: {self.science}")
        print(f"Average: {self.average:.2f}")

# Main logic
students_list = []

for i in range(3):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Name: ")
    
    try:
        english = float(input("English Marks: "))
        math = float(input("Math Marks: "))
        science = float(input("Science Marks: "))
    except ValueError:
        print("Invalid input. Please enter numeric marks.")
        continue

    student = Student(name, english, math, science)
    students_list.append(student)

print("\n--- Student Records ---")
for student in students_list:
    student.display_info()

with open("students_oop.txt", "w") as file:
    for student in students_list:
        file.write(f"Name: {student.name}, English: {student.english}, Math: {student.math}, Science: {student.science}, Average: {student.average:.2f}\n")

print("\nStudent data saved to 'students_oop.txt' successfully.")
