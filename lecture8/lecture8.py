# import os
# script_dir = os.path.dirname(__file__)
# file_path = os.path.join(script_dir, "students.txt")
# new_student = input("Enter the name of the new student: ")
# with open(file_path, "a") as file:
#     file.write("\n"+new_student)
# print(f"{new_student} has been added to the students list.")

# file = open("marks.txt", "w")

# file.write("95\n")
# file.write("65\n")
# file.write("78\n")
# file.write("87\n")
# file.write("82\n")

# file.close()

# file = open("marks.txt", "r")
# total_marks = 0
# length = 0
# for line in file:
#     total_marks += int(line.strip())
#     length += 1
# file.close()
# average_marks = total_marks / length
# print(f"The total marks are: {total_marks}")
# print(f"The average marks are: {average_marks}")

# file = open("marks.txt", "a")
# file.write("Total Marks: " + str(total_marks) + "\n")
# file.write("Average Marks: " + str(average_marks) + "\n")
# file.close()

# notes = open("notes.txt", "w")
# notes.write("Lecture 8: File Handling in Python\n")
# notes.write("1. Opening and Closing Files\n")
# notes.write("2. Reading and Writing Files\n")
# notes.write("3. Appending to Files\n")

# notes.close()

# notes = open("notes.txt", "r")
# content = notes.read()
# print("Content of notes.txt:")
# print(content)
# notes.close()

# notes = open("notes.txt", "a")
# notes.write("\n Towmarrow Learning:\n")
# notes.write("4. File Modes\n")
# notes.write("5. Working with File Paths\n")
# notes.write("6. Exception Handling in File Operations\n")
# notes.close()

# notes = open("notes.txt", "r")
# content = notes.read()
# print("Updated content of notes.txt:")
# print(content)
# notes.close()

students = [
    {"Name": "Ali", "Age": 18, "Marks": 85},
    {"Name": "Sara", "Age": 19, "Marks": 90},
    {"Name": "Ahmed", "Age": 17, "Marks": 80}
]

file = open("students.txt", "w")
for student in students:
    file.write(f"Name: {student['Name']}, Age: {student['Age']}, Marks: {student['Marks']}\n")
file.close()
file = open("students.txt", "r")
content = file.read()
print("Content of students.txt:")
print(content)
file.close()