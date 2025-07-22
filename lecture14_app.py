from flask import Flask, jsonify

app = Flask(__name__)

# 1️⃣ Root Route
@app.route("/")
def home():
    return "Hello, Flask Developer!"

# 2️⃣ /api/info Route
@app.route("/api/info")
def api_info():
    data = {
        "framework": "Flask",
        "version": 1,
        "goal": "API Development"
    }
    return jsonify(data)

# 3️⃣ /api/user/<username> Route
@app.route("/api/user/<username>")
def greet_user(username):
    return jsonify({"message": f"Hello, {username}!"})

if __name__ == "__main__":
    app.run(debug=True)
