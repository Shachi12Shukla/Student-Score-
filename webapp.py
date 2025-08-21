import streamlit as st
import pandas as pd
import pickle
import os

st.title("Get Student Performance Score Prediction and Insights")
st.write("This app predicts the **Math Score** of a student based on demographics, lunch type, test preparation, and reading & writing scores.")

tab1 , tab2 = st.tabs(["***Prediction***" , "***Get Insights About Data***"])

with tab1:
    # st.header('Prediction')
    # Load the trained model
    with open('student_score_model.pkl', 'rb') as f:
        model = pickle.load(f)

        # Input fields
    gender = st.selectbox("Gender", ["female", "male"])
    Ethnic_Background = st.selectbox("Ethnic Background", ["group A", "group B", "group C", "group D", "group E"])
    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"]
        )

    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])


    reading_score = st.slider("Reading Score", 0, 100, 50)
    writing_score = st.slider("Writing Score", 0, 100, 50)

    # Predict button
    if st.button("Predict Math Score"):
        # Create dataframe for input
        input_data = pd.DataFrame({
            'gender': [gender],
            'race_ethnicity': [Ethnic_Background],
            'parental_level_of_education': [parental_level_of_education],
            'lunch': [lunch],
            'test_preparation_course': [test_preparation_course],
            'reading_score': [reading_score],
            'writing_score': [writing_score]
        })

        # Make prediction
        prediction = model.predict(input_data)
            
        st.success(f"Predicted Math Score: **{prediction[0]:.2f}**")


with tab2:
    # st.header('Get Insights About Data')
    # if st.button("Insights" , key=2):
    st.image('insight3.png' , caption=None)
    st.image('insight4.png' , caption=None)
    
    if st.button("Get Insights" , key=3):
        st.info("Students who perform well in reading and writing tend to also perform in math")

    st.image('insight1.png')
    if st.button('Get Insights' , key = 4):
        st.info('Students who complete test preparation course tend to perform higher in math')

    
