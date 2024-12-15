"""
Author: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
Date: 2024-12-12 08:19:53
LastEditors: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
LastEditTime: 2024-12-13 15:29:46
FilePath: app.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
import streamlit as st

from data import *
from utils import avg_value
from utils import get_key
from pickle import load

st.set_page_config("wide")
st.title("Predicted students graduated, dropout, or enrolled")

with st.form("my_form"):
    name = st.text_input("Name:")
    marital_status = st.selectbox("Martial status:", (data_status.values()))
    
    application_mode = st.selectbox("Application mode:", (data_application_mode.values()))
    
    application_order = st.number_input("Application order:", min_value=0, max_value=9)
    
    course = st.selectbox("Course:", (data_course.values()))
    
    attendance = st.radio("Attendance", [data_attendance[0], data_attendance[1]])
    
    previous_qualification = st.selectbox("Previous qualification:", (data_previous_qualification.values()))
    
    previous_qualification_grade = st.number_input("Grade previous qualification:", min_value=0, max_value=100)
    
    mother_qualification = st.selectbox("Mother's qualification:", (data_parents_qualification.values()))

    father_qualification = st.selectbox("Father's qualification:", (data_parents_qualification.values()))
    mother_occupation = st.selectbox("Mother's occupation:", (data_parents_occupation.values()))
    father_occupation = st.selectbox("Father's occupation:", (data_parents_occupation.values()))
    admission_grade = st.number_input("Admission grade:")
    displaced = st.radio("Displaced:", [data_yes_no[0], data_yes_no[1]])
    
    debtor = st.radio("Debtor:", [data_yes_no[0], data_yes_no[1]])
    tuition_fee = st.radio("Tuition fee up to date:", [data_yes_no[0], data_yes_no[1]])
    gender = st.selectbox("Gender:", (data_gender.values()))
    scholarship_holder = st.radio("Scholarship holder:", [data_yes_no[0], data_yes_no[1]])
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
        
        marital_status_key = get_key(data_status, marital_status)
        application_mode_key = get_key(data_application_mode, application_mode)
        course_key = get_key(data_course, course)
        attendance_key = get_key(data_attendance, attendance)
        previous_qualification_key = get_key(data_previous_qualification, previous_qualification)
        mother_qualification_key = get_key(data_parents_qualification, mother_qualification)
        father_qualification_key = get_key(data_parents_qualification, father_qualification)
        mother_occupation_key = get_key(data_parents_occupation, mother_occupation)
        father_occupation_key = get_key(data_parents_occupation, father_occupation)
        displaced_key = get_key(data_yes_no, displaced)
        debtor_key = get_key(data_yes_no, debtor)
        tuition_fee_key = get_key(data_yes_no, tuition_fee)
        gender_key = get_key(data_gender, gender)
        scholarship_holder_key = get_key(data_yes_no, scholarship_holder)
        
        data = [[marital_status_key, application_mode_key, application_order, course_key, attendance_key, previous_qualification_key
                , previous_qualification_grade, mother_qualification_key, father_qualification_key, mother_occupation_key,
                father_occupation_key, admission_grade, displaced_key, debtor_key, tuition_fee_key, gender_key, scholarship_holder_key, age,
                avg_enrolled, avg_approved, avg_grade]]
        
        model = load(open("models/voting_clf_three_labels.pkl", "rb"))
        prediction = model.predict_proba(data)
        
        dropout = prediction[0][0] * 100
        enrolled = prediction[0][1] * 100
        graduated = prediction[0][2] * 100

        if dropout > enrolled and dropout > graduated:
            st.error(f"Maaf,{name} punya kemungkinan dropout sebesar {dropout:.2f}%")
        elif enrolled > dropout and enrolled > graduated:
            st.warning(f"Maaf,{name} punya kemungkinan enrolled sebesar {enrolled:.2f}%")
        elif graduated > dropout and graduated > enrolled:
            st.success(f"{name} punya kemungkinan lulus sebesar {graduated:.2f}%")
    
    
