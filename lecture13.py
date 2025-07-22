import json

# Create dictionary
student = {"name": "Ayesha", "age": 20, "marks": [92, 88, 95]}

# Serialize to JSON and save to file
with open("student.json", "w") as file:
    json.dump(student, file)

# Load JSON back from file
with open("student.json", "r") as file:
    loaded_student = json.load(file)

# Print student's name
print("Student's Name:", loaded_student["name"])
