# name = input("Enter Your Name: ")
# age  = int(input("Enter Your Age: "))
# country = input("Enter Your Country Name:")

# if country == "Pakistan" and age >= 18: 
#     print(f"{name}, you are eligible for a CNIC.")
# elif country == "Pakistan" and age < 18:
#     print(f"{name}, you are not eligible for a CNIC.")
# elif country != "Pakistan":
#     print(f"{name} You are not Pakistani citizen")


number = int(input("Enter any Number: "))

if number > 0 and number % 2 ==0: 
    print("The number is positive and even.")
elif number > 0 and number % 2 != 0:
    print("The number is positive and odd.")
elif number < 0: 
    print("The number is negative.")
elif number == 0:
    print("The number is zero.")