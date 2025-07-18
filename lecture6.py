# def print_greeting():
#     string = "Welcome to Python Functions!"
#     i = 0 
#     while i < 3:
#         print(string) 
#         i += 1

# print_greeting()

# def multiply(a, b):
#     return a * b

# num1 = int(input("Enter 1st Number: "))
# num2 = int(input("Enter 2nd Number: "))

# print(multiply(num1, num2))

# def is_even(num):
#     if num % 2 == 0:
#         print("Your Number is Even")
#     else:
#         print("Your Number is Odd")

# number = int(input("Enter any Number:"))

# is_even(number)

def calculate_average(numbers):
    i = 0
    total = 0
    for number in numbers:
        total += int(number)
        i += 1
    average = total / i
    return average

numbers = [4,6,8,4,6,2]

print(calculate_average(numbers))