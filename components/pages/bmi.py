import streamlit as st

def bmi_form():
    def on_click():
        st.session_state['current_weight'] = st.session_state.current_weight_input
        st.session_state['height'] = st.session_state.height_input


    with st.form("bmi_form"):
        st.number_input('Weight (kg)',key="current_weight_input",value=st.session_state['current_weight'])
        st.number_input('Height (cm)',100,250,key="height_input",value=st.session_state['height'])
        if st.form_submit_button("Submit",on_click=on_click):
            st.session_state['bmi_form_submitted'] += 1
            






