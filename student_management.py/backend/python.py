from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# create database
def get_db():
    return sqlite3.connect("students.db")

# create table
with get_db() as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll TEXT,
        dept TEXT
    )
    """)

# add student
@app.route("/add", methods=["POST"])
def add_student():
    data = request.json
    with get_db() as conn:
        conn.execute(
            "INSERT INTO students (name, roll, dept) VALUES (?, ?, ?)",
            (data["name"], data["roll"], data["dept"])
        )
    return jsonify({"message": "Student added"})

# get students
@app.route("/students", methods=["GET"])
def get_students():
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM students").fetchall()

    students = []
    for r in rows:
        students.append({
            "id": r[0],
            "name": r[1],
            "roll": r[2],
            "dept": r[3]
        })
    return jsonify(students)

# delete student
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_student(id):
    with get_db() as conn:
        conn.execute("DELETE FROM students WHERE id=?", (id,))
    return jsonify({"message": "Student deleted"})

if __name__ == "__main__":
    app.run(debug=True)