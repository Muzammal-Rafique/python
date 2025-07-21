# file = open("data.txt", "r")

# content = file.read()
# print(content)

# file.close()

# file = open("data.txt", "r")

# for line in file:
#     print(line.strip())

# file.close()

# file = open("output.txt", "w")

# file.write("Hello, Python!\n")
# file.write("This is written to a file.\n")
# file.write("Appending more text to the file.\n")
# file.write("This is the last line.\n")
# file.write("This text is successfully added.\n")

# file.close()

# file = open("output.txt", "a")

# file.write("Adding another line.\n")

# file.close()

# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("output.txt", "a") as file:
#     file.write("Another safe write.\n")

total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())

with open("output.txt", "a") as file:
    file.write(f"\nThe sum of numbers is: {total}")
print(f"The sum of numbers is: {total}")

