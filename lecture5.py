# for i in range(1,10):
#     print(i)

# name = input("Enter You Name: ")

# for char in name:
#     print(char)

# numbers = [1,2,3,4,5]

# for number in numbers:
#     print(number)

# line = "Learning Python"
# i = 0

# while i < 5:
#     print(line)
#     i += 1 

total = 0   
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  
    
    total += number  

print(f"The sum of all entered numbers is: {total}")
