# number = input("Enter a number: ")
# try:
#     number = int(number)
#     print(f"You square of the number: {number*number}")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")

# number_1 = input("Enter first number: ")
# number_2 = input("Enter second number: ")

# try:
#     number_1 = int(number_1)
#     number_2 = int(number_2)
#     print(f"The sum of the numbers is: {number_1 / number_2}")
# except ValueError:
#     print("Invalid input! Please enter valid numbers.")
# except ZeroDivisionError:
#     print("Cannot divide by zero. Please enter a non-zero second number.")

# filename = input("Enter the filename to read: ")

# try:
#     with open(filename, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found. Please check the filename and try again.")
# finally:
#     print("Operation completed.")


filename = input("Enter the filename (e.g., input.txt): ")

try:
    with open(filename, "r") as file:
        total_lines = 0
        total_words = 0

        for line in file:
            total_lines += 1
            words = line.split()
            total_words += len(words)

    print(f"\nFile: {filename}")
    print(f"Total Lines: {total_lines}")
    print(f"Total Words: {total_words}")

except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found. Please check the filename and try again.")

finally:
    print("\nProcessing completed.")