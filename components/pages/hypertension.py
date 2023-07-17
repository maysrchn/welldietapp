import streamlit as st
from RiskEngine.RiskEngine import yes_no_converter,family_HT_result_converter
def hypertension_BP_form():

    def on_click():
        st.session_state['current_weight'] = st.session_state.current_weight_input
        st.session_state['height'] = st.session_state.height_input
        st.session_state['SBP'] = st.session_state.SBP_input
        st.session_state['DBP'] = st.session_state.DBP_input

    with st.form("hypertension_BP_form"):
        st.number_input('Weight (kg)',key="current_weight_input",value=st.session_state['current_weight'],disabled = True)
        st.number_input('Height (cm)',100,250,key="height_input",value=st.session_state['height'],disabled = True)
        st.divider()
        st.number_input('Systolic Blood Pressure (mmHg)',key="SBP_input",value=st.session_state['SBP'])
        st.number_input('Diastolic Blood Pressure (mmHg)',key="DBP_input",value=st.session_state['DBP'])
        if st.form_submit_button("Submit",on_click=on_click) and (st.session_state['SBP'] >= 140 or st.session_state['DBP'] >= 90) :
            st.session_state['hypertension_BP_form_submitted'] += 1




def hypertension_low_BP_form():
    options_yes_no = ["Yes", "No"]
    options_family_HT = ["ไม่มีใครเป็น", "เป็น 1 คน", "เป็นทั้งพ่อทั้งแม่"]
    def on_click():
        st.session_state['is_smoke_yes_no']  = st.session_state.is_smoke_input # yes no
        st.session_state.is_smoke = yes_no_converter(st.session_state.is_smoke_yes_no)
        st.session_state['family_HT_yes_no']  = st.session_state.family_HT_input # yes no หมายถึงคำตอบดิบ "ไม่มีใครเป็น", "เป็น 1 คน", "เป็นทั้งพ่อทั้งแม่"
        st.session_state.family_HT=family_HT_result_converter(st.session_state.family_HT_yes_no)
    with st.form("hypertension_low_BP_form"):
        st.radio("คุณสูบบุหรี่หรือไม่", options_yes_no,key="is_smoke_input",index=options_yes_no.index(st.session_state.is_smoke_yes_no))
        st.radio("มี พ่อ แม่ เป็นโรคความดันโลหิตสูง?",options_family_HT,key="family_HT_input",index=options_family_HT.index(st.session_state.family_HT_yes_no))  
        if st.form_submit_button("Submit",on_click=on_click):
            st.session_state['hypertension_low_BP_form_submitted'] += 1


