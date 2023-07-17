import streamlit as st
from RiskEngine.RiskEngine import is_DM,risk_factor_CVD,yes_no_converter

def cvd_chd_equivalent_form():
    options_yes_no = ["Yes", "No"]
    def on_click():
        st.session_state['LDL'] = st.session_state.LDL_input
        st.session_state['is_CVD_yes_no']  = st.session_state.is_CVD_input # yes no
        st.session_state.is_CVD = yes_no_converter(st.session_state.is_CVD_yes_no)
        st.session_state['FBS'] = st.session_state.FBS_input
        st.session_state['twoHr_postprandial'] = st.session_state.twoHr_postprandial_input
        st.session_state['HbA1c'] = st.session_state.HbA1c_input
    with st.form("cvd_chd_equivalent_form"):
        st.number_input('LDL (mg/dL)',key="LDL_input",value=st.session_state['LDL'])
        st.radio("คุณมีโรคหัวใจและหลอดเลือด ? (cardiovascular disease)",options_yes_no,key="is_CVD_input",index=options_yes_no.index(st.session_state.is_CVD_yes_no))
        col1,col2,col3 = st.columns(3)
        with col1:
            st.number_input('FBS (mg/dL)',help="หากท่านไม่ทราบ ให้ใส่ 0",key="FBS_input",value=st.session_state['FBS'])
        with col2:
            st.number_input('2-hour post-prandial (mg/dL) (ถ้ามี)',help="หากท่านไม่ทราบ ให้ใส่ 0",key="twoHr_postprandial_input",value=st.session_state['twoHr_postprandial'])
        with col3:
            st.number_input('HbA1c (%) (ถ้ามี)',help="หากท่านไม่ทราบ ให้ใส่ 0",key="HbA1c_input",value=st.session_state['HbA1c'])
        if st.form_submit_button("Submit",on_click=on_click) :
            st.session_state['cvd_chd_equivalent_form_submitted'] += 1
            if (st.session_state.is_CVD == True )or (is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c) ==True ):
                st.session_state['cvd_chd_equivalent_form_get_score_if_finish'] += 1

def cvd_risk_factor_form():
    options_yes_no = ["Yes", "No"]
    def on_click():
        st.session_state['is_smoke_yes_no']  = st.session_state.is_smoke_input # yes no
        st.session_state.is_smoke = yes_no_converter(st.session_state.is_smoke_yes_no)
        st.session_state['SBP'] = st.session_state.SBP_input
        st.session_state['DBP'] = st.session_state.DBP_input
        st.session_state['is_HT_medicinetreat_yes_no'] = st.session_state.is_HT_medicinetreat_input  # yes no
        st.session_state.is_HT_medicinetreat = yes_no_converter(st.session_state.is_HT_medicinetreat_yes_no)
        st.session_state['HDL'] = st.session_state.HDL_input
        st.session_state['family_CHD_yes_no'] = st.session_state.family_CHD_input  # yes no
        st.session_state.family_CHD = yes_no_converter(st.session_state.family_CHD_yes_no)

    with st.form("cvd_risk_factor_form"):
        st.number_input('Systolic Blood Pressure (mmHg)',key="SBP_input",value=st.session_state['SBP'],disabled=True)
        st.number_input('Diastolic Blood Pressure (mmHg)',key="DBP_input",value=st.session_state['DBP'],disabled=True)
        st.divider()
        st.number_input('HDL (mg/dL)',key="HDL_input",value=st.session_state['HDL'])
        st.radio("คุณสูบบุหรี่หรือไม่", options_yes_no,key="is_smoke_input",index=options_yes_no.index(st.session_state.is_smoke_yes_no))
        st.radio("คุณกำลังรับประทานยาควบคุมความดันโลหิตสูงหรือไม่",options_yes_no,key="is_HT_medicinetreat_input",index=options_yes_no.index(st.session_state.is_HT_medicinetreat_yes_no))
        st.radio("พ่อแม่ พี่ น้อง มีโรคหัวใจ? ที่เริ่มเป็นก่อนอายุ <55 ปี(ชาย) อายุ <65 ปี(หญิง)",options_yes_no,key="family_CHD_input",index=options_yes_no.index(st.session_state.family_CHD_yes_no))
        if st.form_submit_button("Submit",on_click=on_click) :
            st.session_state['cvd_risk_factor_form_submitted'] += 1
            if risk_factor_CVD(st.session_state.is_smoke,st.session_state.SBP,st.session_state.DBP,st.session_state.is_HT_medicinetreat,st.session_state.HDL,st.session_state.family_CHD,st.session_state.gender,st.session_state.age) <2:
                st.session_state['cvd_risk_factor_form_get_score_if_finish'] += 1




    
def cvd_score_form():
    def on_click():
        st.session_state['TC'] = st.session_state.TC_input
    with st.form("cvd_score_form"):
        st.number_input('Total Cholesteral (mg/dL)',key="TC_input",value=st.session_state['TC'])
        if st.form_submit_button("Submit",on_click=on_click):
            st.session_state['cvd_score_form_submitted'] += 1
            st.session_state['cvd_score_form_get_score_if_finish'] += 1




