from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/student", methods=["GET"])
def get_student():
    student = {
        "name": "Ali",
        "age": 21,
        "marks": [85, 90, 78]
    }
    return jsonify(student)

if __name__ == "__main__":
    app.run(debug=True)
