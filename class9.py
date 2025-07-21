# try:
#     num = int(input("Enter a number: "))
#     print(f"You entered: {num}")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")

# try:
#     file = open("data.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found!")
# finally:
#     print("Execution complete.")

# try:
#     num = int(input("Enter a number: "))
#     result = 50 / num
#     print(f"The result is: {result}")
# except ValueError:
#     print("Invalid input, please enter a number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input.")
# else:
#     print(f"Thank you for entering {num}.")

filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name.")
finally:
    print("File read attempt complete.")
