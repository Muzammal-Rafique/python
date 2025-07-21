def add_expense():
    try:
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        date = input("Enter expense date (YYYY-MM-DD): ")

        with open("expenses_data.txt", "a") as file:
            file.write(f"Description: {description}, Amount: {amount:.2f}, Date: {date}\n")

        print(f"Expense '{description}' added successfully!\n")

    except ValueError:
        print("Invalid input! Please enter a valid amount.\n")

def view_expenses():
    try:
        with open("expenses_data.txt", "r") as file:
            data = file.readlines()
            if data:
                for line in data:
                    print(line.strip())
            else:
                print("No expenses found.\n")
    except FileNotFoundError:
        print("No expenses data file found. Add expenses first.\n")

def calculate_total_expenses():
    try:
        total = 0.0
        with open("expenses_data.txt", "r") as file:
            data = file.readlines()
            for line in data:
                parts = line.split(", ")
                amount_part = parts[1].split(": ")[1]
                total += float(amount_part)

        print(f"Total expenses: {total:.2f}\n")
    except FileNotFoundError:
        print("No expenses data file found. Add expenses first.\n")

while True:
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total_expenses()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.\n")