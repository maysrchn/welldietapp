import streamlit as st
from RiskEngine.RiskEngine import BMI_calculation,yes_no_converter
def diabetes_risk_score_form():
    options_yes_no = ["Yes", "No"]
    def on_click():
        st.session_state['family_DM_yes_no'] = st.session_state.family_DM_input
        st.session_state.family_DM=yes_no_converter(st.session_state.family_DM_yes_no)
        st.session_state['is_HT_yes_no'] = st.session_state.is_HT_input
        st.session_state.is_HT=yes_no_converter(st.session_state.is_HT_yes_no)
        st.session_state['waist'] = st.session_state.waist_input


    with st.form("diabetes_risk_factor_form"):
        st.number_input('BMI (kg/sqm)',value=BMI_calculation(st.session_state['current_weight'],st.session_state['height']),disabled = True)
        st.number_input('Waist (inches)',key="waist_input",value=st.session_state['waist'])
        st.radio("คุณเป็นโรคความดันโลหิตสูงหรือไม่",options_yes_no,key="is_HT_input",index=options_yes_no.index(st.session_state.is_HT_yes_no))
        st.radio("มี พ่อ แม่ พี่ หรือ น้อง เป็นโรคเบาหวาน?",options_yes_no,key="family_DM_input",index=options_yes_no.index(st.session_state.family_DM_yes_no))

        if st.form_submit_button("Submit",on_click=on_click):
            st.session_state['diabetes_risk_score_form_submitted'] += 1


