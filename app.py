"""
Author: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
Date: 2024-12-12 08:19:53
LastEditors: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
LastEditTime: 2024-12-13 01:38:58
FilePath: app.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
import streamlit as st
from data import *
from utils import avg_value

st.set_page_config("wide")
st.title("Predicted students graduated, dropout, or enrolled")

with st.form("my_form"):
    name = st.text_input("Name:")
    marital_status = st.selectbox("Martial status:", (data_status.values()))
    
    application_mode = st.selectbox("Application mode:", (data_application_mode.values()))
    
    application_order = st.slider('Pick a number', 0, 9)
    
    course = st.selectbox("Course:", (data_course.values()))
    
    attendance = st.radio("Attendance", ["Evening","Daytime"])
    
    previous_qualification = st.selectbox("Previous qualification:", (data_previous_qualification.values()))
    
    previous_qualification_grade = st.number_input("Grade previous qualification:")
    
    mother_qualification = st.selectbox("Mother's qualification:", (data_parents_qualification.values()))

    father_qualification = st.selectbox("Father's qualification:", (data_parents_qualification.values()))
    mother_occupation = st.selectbox("Mother's occupation:", (data_parents_occupation.values()))
    father_occupation = st.selectbox("Father's occupation:", (data_parents_occupation.values()))
    admission_grade = st.number_input("Admission grade:")
    displaced = st.radio("Displaced:", ["Yes", "No"])
    
    debtor = st.radio("Debtor:", ["Yes", "No"])
    tuition_fee = st.radio("Tuition fee up to date:", ["Yes", "No"])
    gender = st.selectbox("Gender:", ("Male", "Female"))
    scholarship_holder = st.radio("Scholarship holder:", ["Yes", "No"])
    age = st.number_input("Age:")
    curricular_units_1st_sem_enrolled = st.number_input("Curricular units 1st sem enrolled:")
    curricular_units_1st_sem_approved = st.number_input("Curricular units 1st sem approved:")
    curricular_units_1st_sem_grade = st.number_input("Curricular units 1st sem grade:")
    
    curricular_units_2nd_sem_enrolled = st.number_input("Curricular units 2nd sem enrolled:")
    curricular_units_2nd_sem_approved = st.number_input("Curricular units 2nd sem approved:")
    curricular_units_2nd_sem_grade = st.number_input("Curricular units 2nd sem grade:")
    
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        avg_enrolled = avg_value(int(curricular_units_1st_sem_grade), int(curricular_units_2nd_sem_grade))
        avg_approved = avg_value(int(curricular_units_1st_sem_approved), int(curricular_units_2nd_sem_approved))
        avg_grade = avg_value(int(curricular_units_1st_sem_grade), int(curricular_units_2nd_sem_grade))
        
        
    
    
