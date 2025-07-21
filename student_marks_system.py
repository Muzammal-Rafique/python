def add_student():
    try:
        name = input("Enter student name: ")

        english = int(input("Enter English marks: "))
        math = int(input("Enter Math marks: "))
        science = int(input("Enter Science marks: "))

        average = (english + math + science) / 3

        with open("students_data.txt", "a") as file:
            file.write(f"Name: {name}, English: {english}, Math: {math}, Science: {science}, Average: {average:.2f}\n")

        print(f"{name}'s data saved successfully!\n")

    except ValueError:
        print("Invalid input! Please enter numeric values for marks.\n")

def view_students():
    try:
        with open("students_data.txt", "r") as file:
            data = file.readlines()
            if data:
                for line in data:
                    print(line.strip())
            else:
                print("No student data found.\n")
    except FileNotFoundError:
        print("No student data file found. Add students first.\n")

while True:
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.\n")
