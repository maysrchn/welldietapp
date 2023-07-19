import streamlit as st
from .hypertension import hypertension_BP_form,hypertension_low_BP_form

def HypertensionScreener():
    hypertension_BP_form()
    if ((st.session_state['SBP'] >= 140 or st.session_state['DBP'] >= 90) is False )and(st.session_state['SBP'] > 0 or st.session_state['DBP'] >0) : 
        hypertension_low_BP_form()
#ไม่ความดันสูง ต้องประเมินต่อ และความดันต้องไม่เป็น  0 ถึงจะ activate form next






