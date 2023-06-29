import streamlit as st
st.title('Well Diet')
st.subheader('NCDs Risk Detection and Lifestyle Modification Therapy')
st.caption('by :blue[INVITRACE]')

st.selectbox('Gender',['Male','Female'])
st.slider('Age', 18,120)
st.number_input('Current Weight (kg)')
st.number_input('Height (cm)')
st.number_input('Waist (inches)')
st.number_input('Triglyceride (mg/dL)')
st.number_input('HDL (mg/dL)')
st.number_input('FBS (mg/dL)')
st.number_input('ค่าน้ำตาลปลายนี้ว หลังอดอาหาร (mg/dL) (ถ้ามี)')
st.number_input('Systolic Blood Pressure (mmHg)')
st.number_input('Diastolic Blood Pressure (mmHg)')
st.number_input('Total Cholesteral (mg/dL)')
st.number_input('LDL (mg/dL)')
st.number_input('ค่าน้ำตาล หลังทานอาหาร 2 ชั่วโมง  (mg/dL) (ถ้ามี)')
st.number_input('HbA1c (%) (ถ้ามี)')


# TG = 100
# HDL = 50
# FBS = 90
# fastingDTX = 0                      #ถ้ามี
# SBP = 92
# DBP = 53
# TC = 100
# LDL = 98
# twoHr_postprandial = 0              #ถ้ามี
# HbA1c = 0         
# st.checkbox('yes')

# st.radio('Pick your gender',['Male','Female'])

# st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
# st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
# st.slider('Pick a number', 0,50)

# st.text_input('Email address')
# st.date_input('Travelling date')



st.button('Click')

#cd /Users/may/Desktop/welldiet.py/ 
#streamlit run streamlit_welldiet.py