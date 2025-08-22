# Student Performance Score Prediction Project
An ML-DS project to understand how the performance of a student depends on certain factors. 
App is deployed and hosted at - https://student-performance-score-prediction.streamlit.app/

### Dataset Link https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

## Dataset Details 
- 1000 rows and 8 columns 
- gender : sex of students  -> (Male/female)
- race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)
- parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)
- lunch : having lunch before test (standard or free/reduced) 
- test preparation course : complete or not complete before test
- math score
- reading score
- writing score

---

## 🚀 Features

* Data preprocessing & visualization
* Linear Regression model for score prediction
* Model persistence with **Pickle (.pkl)**
* Interactive web app for predictions
* Visual insights (`insights.png`, `insights2.png`)

---

## 📂 Project Structure

```
Student-Score-
│-- app.ipynb              # Jupyter notebook with training & analysis
│-- webapp.py              # Web application for predictions
│-- student_score_model.pkl # Saved trained model
│-- requirements.txt       # Python dependencies
│-- insights.png           # Visualization 1
│-- insights2.png          # Visualization 2
│-- data/                  # Dataset folder
│-- README.md              # Project documentation
│-- .git/                  # Git repository (if initialized)
```

## ⚙️ Installation & Setup

1. Clone the repository or extract the zip file.

```bash
git clone <https://github.com/Shachi12Shukla/Student-Score->
cd Student-Score-
```

2. Create a virtual environment (optional but recommended).

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3. Install dependencies:

```
bash
pip install -r requirements.txt
```

## ▶️ Running the Project

### 1. Jupyter Notebook (Model Training & Analysis)

```bash
jupyter notebook app.ipynb
```

### 2. Web Application (Prediction Interface)

```bash
python webapp.py
```

## 📊 Model Performance

* **R² Score:** \~0.876
* **Mean Absolute Error (MAE):** \~4.42
* **Mean Squared Error (MSE):** \~30.89
* **Root Mean Squared Error (RMSE):** \~5.56

---

## 🖼️ Visual Insights

* `insights.png` – Relation between test preparation course and average score & gender and average score
* `insights2.png` – Relation between lunch and average score

---

## 📌 Tech Stack

* **Python** (Pandas, NumPy, Scikit-learn, Matplotlib and Seaborn)
* **Streamlit** (for web app)
* **Jupyter Notebook** (for training & analysis)

---

## 🤝 Contribution

Contributions, issues, and feature requests are welcome!



