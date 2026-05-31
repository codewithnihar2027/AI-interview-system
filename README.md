# 🎯 AI Interview System

An AI-powered Interview Preparation Platform built using Python, Streamlit, and Google Gemini API.

The system generates interview questions, evaluates answers, provides ideal solutions, supports voice answers, and tracks user performance through a dashboard.

---

## 🚀 Features

### 📌 Interview Question Generation
- Generate interview questions based on:
  - Role
  - Difficulty Level
  - Interview Type

### ✍️ Text Answer Mode
- Type answers directly in the editor
- AI evaluates the response

### 🎤 Voice Answer Mode
- Record answers using microphone
- Speech-to-Text conversion
- AI evaluates spoken responses

### 📊 AI Evaluation
- Score out of 100
- Strengths
- Weaknesses
- Suggestions for improvement

### 📖 Ideal Answer Generator
- View a model answer after evaluation
- Beginner-friendly explanations
- Example-based solutions

### 📈 Performance Dashboard
- Total Questions Attempted
- Average Score
- Highest Score
- Recent Attempt History

### 📄 Evaluation Report Download
- Download interview evaluation reports

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Model
- Google Gemini API

### Speech Processing
- SpeechRecognition
- Streamlit Mic Recorder

### Data Storage
- JSON

### Visualization
- Pandas

---

## 📂 Project Structure

```text
AI-Interview-System/
│
├── frontend/
│   └── app.py
│
├── backend/
│   ├── question_generator.py
│   ├── evaluator.py
│   ├── parser.py
│   ├── speech_to_text.py
│   ├── solution_generator.py
│   ├── history.py
│   └── dashboard.py
│
├── data/
│   └── history.json
│
├── config.py
├── requirements.txt
└── README.md
```

## 🎯 Future Improvements

- User Authentication
- Leaderboard
- Interview Analytics
- PDF Report Generation
- Mock Interview Simulation
- Progress Tracking Graphs

---

## 👨‍💻 Author

Meghna Rao

B.Tech CSE (AI & ML)

Passionate about AI, Data Science, and Software Development.

---
