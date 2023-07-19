import streamlit as st

def demographic_form():
    genderlist = ['male','female']
    def on_click():
        st.session_state['fullname'] = st.session_state.fullname_input
        st.session_state['gender'] = st.session_state.gender_input
        st.session_state['age'] = st.session_state.age_input

    with st.form("demographic_form"):
        st.text_input('Full name',help="ใส่ชื่อเพื่อแสดงชื่อในหน้าผลการประเมิน",key="fullname_input",value=st.session_state['fullname'])
        col1,col2 = st.columns(2)
        with col1:
            st.selectbox('Gender',['male','female'],key="gender_input",index=genderlist.index(st.session_state['gender']))
            
        with col2:
            st.slider('Age', 18,120,key="age_input",value=st.session_state['age'])
        if st.form_submit_button("Submit",on_click=on_click):
            st.session_state['profile_form_submitted'] += 1
            

