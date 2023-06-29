import streamlit as st
st.title('Well Diet')
st.subheader('NCDs Risk Detection and Lifestyle Modification Therapy')

st.selectbox('Gender',['Male','Female'])
 st.slider('AgePick a number', 18,120)
st.number_input('Current Weight')
st.number_input('Height')
st.number_input('Waist')

st.number_input('Triglyceride')
st.number_input('HDL')
st.number_input('FBS')
st.number_input('ค่าน้ำตาลปลายนี้ว หลังอดอาหาร (ถ้ามี)')
st.number_input('Systolic Blood Pressure')
st.number_input('Diastolic Blood Pressure')
st.number_input('Total Cholesteral')
st.number_input('LDL')
st.number_input('ค่าน้ำตาล หลังทานอาหาร 2 ชั่วโมง (ถ้ามี)')
st.number_input('HbA1c')


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