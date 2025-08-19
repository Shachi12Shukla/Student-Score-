# 📘 Student Score Prediction

This project predicts **student scores based on study hours** using a Linear Regression model. It includes data preprocessing, model training, evaluation, and a simple web application for predictions.

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

---

## ⚙️ Installation & Setup

1. Clone the repository or extract the zip file.

```bash
git clone <repo-url>
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

The model performs well for a simple linear regression on study hours vs. scores.

---

## 🖼️ Visual Insights

* `insights.png` – Correlation between study hours and scores
* `insights2.png` – Regression line fit visualization

---

## 📌 Tech Stack

* **Python** (Pandas, NumPy, Scikit-learn, Matplotlib)
* **Streamlit** (for web app)
* **Jupyter Notebook** (for training & analysis)

---

## 🤝 Contribution

Contributions, issues, and feature requests are welcome!



