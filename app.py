from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
import pickle
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

# Load the LSTM model
model = load_model("model/career_lstm_model.h5")

# Load skill mapping
with open("model/skill_mapping3.pkl", "rb") as f:
    skill_mapping = pickle.load(f)

# Database file
DB_FILE = "database/career_skills_final.db"


def get_skills_for_career(career):

    conn = sqlite3.connect(DB_FILE)

    cursor = conn.cursor()

    print(f"Searching for skills for career: {career}")

    cursor.execute(
        "SELECT skills FROM career_skills WHERE career = ?",
        (career,)
    )

    result = cursor.fetchall()

    skills = []

    for row in result:

        skills.extend(row[0].split(","))

    print(f"Found skills: {skills}")

    conn.close()

    return skills


def get_course_recommendations(skills):

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    if not skills:
        return {}

    placeholders = ",".join(["?"] * len(skills))

    cursor.execute(
    "SELECT skills FROM career_skills WHERE career = ?",
    (career,)
)

    courses = {
        skill: link
        for skill, link in cursor.fetchall()
    }

    conn.close()

    return courses


# Home Route
@app.route("/")
def home():
    return render_template("login.html")


# Signup Route
@app.route("/signup")
def signup():
    return render_template("signup.html")


# Index Route
@app.route("/index")
def index():
    return render_template("index.html")


# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    career = data.get("career", "").strip()

    if not career:
        return jsonify(
            {"error": "No career provided"}
        ), 400

    # Fetch skills
    skills_list = get_skills_for_career(career)

    if not skills_list:
        return jsonify(
            {"error": "No skills found for the given career"}
        ), 404

    # Fetch course recommendations
    course_recommendations = get_course_recommendations(
        skills_list
    )

    response = {
        "career": career,
        "skills": skills_list,
        "courses": course_recommendations
    }

    return jsonify(response)


if __name__ == "__main__":

    print("Flask server is running...")

    app.run(debug=True)