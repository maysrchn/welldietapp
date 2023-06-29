import streamlit as st
st.title('Well Diet')
st.header('NCDs Risk Detection and Lifestyle Modification Therapy')

st.selectbox('Gender',['Male','Female'])
st.number_input('Age', 18,120)
st.number_input('Current Weight', 30,300)
st.number_input('Height')
st.number_input('Waist')

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