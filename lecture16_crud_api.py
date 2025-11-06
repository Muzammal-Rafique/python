from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database
students = [
    {"id": 1, "name": "Ali", "age": 21},
    {"id": 2, "name": "Ayesha", "age": 22},
]

# READ - Get all students
@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(students)

# READ - Get a single student by ID
@app.route("/api/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

# CREATE - Add a new student
@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json()
    new_id = students[-1]["id"] + 1 if students else 1
    new_student = {"id": new_id, "name": data["name"], "age": data["age"]}
    students.append(new_student)
    return jsonify(new_student), 201

# UPDATE - Update a student
@app.route("/api/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        student["name"] = data.get("name", student["name"])
        student["age"] = data.get("age", student["age"])
        return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

# DELETE - Delete a student
@app.route("/api/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message": "Student deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
