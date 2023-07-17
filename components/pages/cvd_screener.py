import streamlit as st

from RiskEngine.RiskEngine import is_DM,risk_factor_CVD
from .cvd import cvd_chd_equivalent_form,cvd_risk_factor_form,cvd_score_form
def CVDScreener():
    cvd_chd_equivalent_form()
    if (st.session_state.is_CVD == True )or (is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c) ==True ):
        return None
    if (st.session_state['cvd_chd_equivalent_form_submitted'] > 0) and((st.session_state.is_CVD == True )or (is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c) ==True ) is not True): # >0 หมายถึง กดปุ่มsubmit นับ 1 และ เข้าเงื่อไขที่ต้องประเมินต่อ
        cvd_risk_factor_form()
        
    if risk_factor_CVD(st.session_state.is_smoke,st.session_state.SBP,st.session_state.DBP,st.session_state.is_HT_medicinetreat,st.session_state.HDL,st.session_state.family_CHD,st.session_state.gender,st.session_state.age) <2:
        return None
    if (st.session_state['cvd_risk_factor_form_submitted'] >0 )and risk_factor_CVD(st.session_state.is_smoke,st.session_state.SBP,st.session_state.DBP,st.session_state.is_HT_medicinetreat,st.session_state.HDL,st.session_state.family_CHD,st.session_state.gender,st.session_state.age) >1:
        cvd_score_form()
# >0 หมายถึง กดปุ่มsubmit นับ 1 และ เข้าเงื่อไขที่ต้องประเมินต่อ



#form_submitted ถ้าได้ค่า 1  เมื่อไหร่ แสดงว่ากดปุ่มsubmit แล้ว 


