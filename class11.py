# class Student:
#     def __init__(self, name, age):
#         self.name = name      # Attribute
#         self.age = age

#     def greet(self):          # Method
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# # Creating an object
# student1 = Student("Ali", 20)
# student1.greet()    # Calls the greet method

# class Student:
#     def __init__(self, name, english, math, science):
#         self.name = name
#         self.english = english
#         self.math = math
#         self.science = science
#         self.average = (english + math + science) / 3

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"English: {self.english}, Math: {self.math}, Science: {self.science}")
#         print(f"Average: {self.average:.2f}")

# # Create student object
# student1 = Student("Ali", 85, 90, 78)
# student1.display_info()


# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display_info(self):
#         line = (f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
#         file = open("new_students.txt", "a")
#         file.write(line + "\n")
#         file.close()

# student1 = Student("Ali", 18, 85)
# student1.display_info()

