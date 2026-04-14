# 🚀 AI-Based Skill Gap Analyzer using NLP

## 📌 Overview

This project uses NLP techniques such as TF-IDF vectorization and cosine similarity to analyze and compare skill sets.

SkillGap Analyzer is a simple yet effective tool that helps students and job seekers identify the gap between their current skills and the skills required for a desired job role.


It compares user-input skills with predefined job role requirements and provides:

* Matched skills
* Missing skills
* Match percentage
* Improvement suggestions

---

## 🎯 Problem Statement

Many students apply for jobs without knowing whether their skills match industry requirements. This leads to confusion, lack of direction, and missed opportunities.

This project solves that problem by clearly showing what skills are missing and how to improve.

---

## 💡 Solution

The system:

1. Takes user skills as input
2. Allows selection of a target job role
3. Compares user skills with required skills
4. Calculates a match score
5. Suggests skills to improve

---

## ⚙️ Features

* ✅ Skill input (comma-separated)
* ✅ Multiple job roles support
* ✅ Skill matching system
* ✅ Match percentage calculation
* ✅ Missing skills identification
* ✅ Simple and user-friendly interface

---

## 🛠️ Tech Stack

* Python
* JSON (for storing job roles)

---

## 📂 Project Structure

```
skillgap-analyzer/
│── main.py
│── roles.json
│── README.md
│── report.pdf
│── screenshots/
```

---

## ▶️ How to Run

### Step 1: Clone the repository

```
git clone https://github.com/your-username/skillgap-analyzer.git
```

### Step 2: Navigate to project folder

```
cd skillgap-analyzer
```

### Step 3: Run the program

```
python main.py
```

---

## 📊 Example Output

```
Enter your skills: Python, Excel

Target Role: Data Analyst

Matched Skills: Python, Excel  
Missing Skills: SQL, Power BI, Statistics  
Match Score: 40%

Suggestion:
Focus on learning: SQL, Power BI, Statistics
```

---

## 🧠 How It Works

* Skills are converted to lowercase for accurate comparison
* Matching is done using list comparison
* Score is calculated using:

```
Match Score = (Matched Skills / Total Required Skills) × 100
```

---

## ⚠️ Limitations

* Manual skill input (no resume upload yet)
* Basic string matching (no advanced NLP)
* Limited job roles

---

## 🔮 Future Improvements

* Resume upload (PDF parsing)
* AI-based skill suggestions
* Web interface (Flask / Streamlit)
* Integration with job portals

---

## 📚 Learning Outcomes

* Applied Python to solve a real-world problem
* Learned data handling using JSON
* Improved logical thinking and problem-solving skills
* Understood importance of skill-based analysis

---

## 👨‍💻 Author

Shivam Rai (25BAI11241)

---

## ⭐ Acknowledgement

This project was developed as part of the **BYOP (Bring Your Own Project)** initiative to apply programming concepts to real-world problems.
