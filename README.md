🎯 Career-Based Skill Recommendation System

An AI-powered web application that recommends personalized skills and generates career roadmaps using an LSTM-based Machine Learning model.

Developed by: Anjana K & Team
Institution: Vimal Jyothi Engineering College
Platform: Web Application (Flask + Python)

📌 About the Project
Finding the right career path can be overwhelming — especially for students and fresh graduates. This system solves that problem by letting users search for any career and instantly receiving a personalized roadmap of skills, courses, and steps needed to achieve that goal.
The core of the system is an LSTM (Long Short-Term Memory) model trained on career-skill data, which intelligently maps careers to the most relevant skills and learning paths.

✨ Features
1. 🔍 Career Skill Recommendation

User types in a career (e.g., "Data Scientist", "Web Developer")
System recommends the most relevant skills needed for that career
Powered by a trained LSTM model

2. 🗺️ Personalized Career Roadmap

Generates a step-by-step roadmap for the chosen career
Shows what to learn first, second, and so on
Tailored to the specific career input

3. 📚 Course Recommendations

Suggests relevant courses for each skill
Helps users know exactly where to learn

4. 📊 Skill Progress Tracking

Users can track which skills they have completed
Visual progress through their career roadmap

5. 🔐 User Authentication

Secure Login and Signup system
Personal dashboard for each user
Data stored using SQLite database


🧠 Machine Learning Model
DetailInfoModelLSTM (Long Short-Term Memory)FrameworkTensorFlow / KerasModel Filecareer_lstm_model.h5Tokenizertokenizer.pklSkill Mappingskill_mapping3.pklDatabasecareer_skills_final.db (SQLite)
The LSTM model was trained on a career-skills dataset to learn the relationship between careers and the skills required. It uses sequence modeling to generate contextually relevant skill recommendations.

🛠️ Tech Stack
LayerTechnologyBackendPython, FlaskML ModelTensorFlow, Keras (LSTM)FrontendHTML, CSS, JavaScriptDatabaseSQLiteModel SerializationPickle (.pkl), HDF5 (.h5)

📁 Project Structure
Career-Based-Skill-Recommendation-System/
│
├── app.py                    # Main Flask application
├── train.py                  # LSTM model training script
├── career_lstm_model.h5      # Trained LSTM model
├── tokenizer.pkl             # Tokenizer for text processing
├── skill_mapping3.pkl        # Career to skill mapping
├── career_skills_final.db    # SQLite database
├── index.html                # Main dashboard page
├── login.html                # Login page
├── signup.html               # Signup page
├── requirements.txt          # Python dependencies
└── README.md

🚀 How It Works
User enters a career name
        ↓
Input is tokenized and processed
        ↓
LSTM model predicts relevant skills
        ↓
Skill mapping generates full roadmap
        ↓
Courses recommended for each skill
        ↓
User can track their progress

⚙️ Setup & Installation
Prerequisites

Python 3.x
pip

Steps
bash# Clone the repository
git clone https://github.com/ANJANA-K1122/Career-Based-Skill-Recommendation-System

# Navigate to the project folder
cd Career-Based-Skill-Recommendation-System

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
Then open your browser and go to:
http://localhost:5000

📦 Dependencies
Key libraries used (see requirements.txt for full list):

Flask
TensorFlow
Keras
Scikit-learn
SQLite3
Pickle


🎓 Academic Context
This project was developed as an academic project at Vimal Jyothi Engineering College to address the real-world challenge of career guidance for students using Artificial Intelligence and Machine Learning.

📄 License
This project is for academic purposes. All rights reserved © Anjana K, Vimal Jyothi Engineering College.
