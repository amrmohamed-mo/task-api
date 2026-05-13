from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Study Docker",
        "completed": False
    },
    {
        "id": 2,
        "title": "Learn Git",
        "completed": True
    }
]

@app.route("/")
def home():
    return "Task API is Running"

@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)