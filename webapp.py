import streamlit as st
import pandas as pd
import os

# Load the trained model
model = os.load("student_score_model.pkl")

st.title("📊 Student Math Score Prediction App")

st.write("This app predicts the **Math Score** of a student based on demographics, lunch type, test preparation, and reading & writing scores.")

# Input fields
gender = st.selectbox("Gender", ["female", "male"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
)
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])

# ✅ New sliders for Reading & Writing Scores
reading_score = st.slider("Reading Score", 0, 100, 50)
writing_score = st.slider("Writing Score", 0, 100, 50)

# Predict button
if st.button("Predict Math Score"):
    # Create dataframe for input
    input_data = pd.DataFrame({
        'gender': [gender],
        'race_ethnicity': [race_ethnicity],
        'parental_level_of_education': [parental_level_of_education],
        'lunch': [lunch],
        'test_preparation_course': [test_preparation_course],
        'reading_score': [reading_score],
        'writing_score': [writing_score]
    })

    # Make prediction
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Math Score: **{prediction[0]:.2f}**")
