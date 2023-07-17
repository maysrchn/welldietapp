import streamlit as st
from .hypertension import hypertension_BP_form,hypertension_low_BP_form

def HypertensionScreener():
    hypertension_BP_form()
    if 1<=st.session_state['SBP'] < 140 or 1<=st.session_state['DBP'] < 90:
        hypertension_low_BP_form()







