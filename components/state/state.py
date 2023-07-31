import streamlit as st

def initialize_state():

    if "streamlit_menu" not in st.session_state:
        st.session_state.streamlit_menu = "Profile"
    if "fullname" not in st.session_state:
        st.session_state.fullname = ""
    if "gender" not in st.session_state:
        st.session_state.gender = "male"
    if "age" not in st.session_state:
        st.session_state.age = 18
    if "current_weight" not in st.session_state:
        st.session_state.current_weight = 0
    if "height" not in st.session_state:
        st.session_state.height = 100
    if "waist" not in st.session_state:
        st.session_state.waist = 0
    if "TG" not in st.session_state:
        st.session_state.TG = 0
    if "HDL" not in st.session_state:
        st.session_state.HDL = 0
    if "FBS" not in st.session_state:
        st.session_state.FBS = 0
    if "fastingDTX" not in st.session_state:
        st.session_state.fastingDTX = 0
    if "physical_activity" not in st.session_state:
        st.session_state.physical_activity = "sedentary"
    if "goal_weight" not in st.session_state:
        st.session_state.goal_weight = 0
    if "current_food_record" not in st.session_state:
        st.session_state.current_food_record = 0
    if "SBP" not in st.session_state:
        st.session_state.SBP = 0
    if "DBP" not in st.session_state:
        st.session_state.DBP = 0
    if "TC" not in st.session_state:
        st.session_state.TC = 0
    if "LDL" not in st.session_state:
        st.session_state.LDL = 0
    if "twoHr_postprandial" not in st.session_state:
        st.session_state.twoHr_postprandial = 0
    if "HbA1c" not in st.session_state:
        st.session_state.HbA1c = 0
    if "LDL" not in st.session_state:
        st.session_state.LDL = 0
    if "family_DM" not in st.session_state:
        st.session_state.family_DM = False
    if "family_DM_yes_no" not in st.session_state:
        st.session_state.family_DM_yes_no = "No"


    if "family_HT" not in st.session_state:
        st.session_state.family_HT = 0
    if "family_HT_yes_no" not in st.session_state:
        st.session_state.family_HT_yes_no = "ไม่มีใครเป็น"



    if "family_CHD" not in st.session_state:
        st.session_state.family_CHD = False
    if "family_CHD_yes_no" not in st.session_state:
        st.session_state.family_CHD_yes_no = "No"


    if "is_HT" not in st.session_state:
        st.session_state.is_HT = False
    if "is_HT_yes_no" not in st.session_state:
        st.session_state.is_HT_yes_no = "No"


    if "is_HT_medicinetreat" not in st.session_state:
        st.session_state.is_HT_medicinetreat = False
    if "is_HT_medicinetreat_yes_no" not in st.session_state:
        st.session_state.is_HT_medicinetreat_yes_no = "No"

    if "history_GDM_Macrosomia" not in st.session_state:
        st.session_state.history_GDM_Macrosomia = False
    if "history_impaired_glucose" not in st.session_state:
        st.session_state.history_impaired_glucose = False
    if "is_CVD" not in st.session_state:
        st.session_state.is_CVD = False
    if "is_CVD_yes_no" not in st.session_state:
        st.session_state.is_CVD_yes_no = "No"

    if "is_PCOS" not in st.session_state:
        st.session_state.is_PCOS = False
    if "is_smoke" not in st.session_state:
        st.session_state.is_smoke = False
    if "is_smoke_yes_no" not in st.session_state:
        st.session_state.is_smoke_yes_no = "No"
    if "profile_form_submitted" not in st.session_state:
        st.session_state.profile_form_submitted = 0
    if "bmi_form_submitted" not in st.session_state:
        st.session_state.bmi_form_submitted = 0
    if "weightcontrol_form_submitted" not in st.session_state:
        st.session_state.weightcontrol_form_submitted = 0
    if "hypertension_BP_form_submitted" not in st.session_state:
        st.session_state.hypertension_BP_form_submitted = 0
    if "hypertension_low_BP_form_submitted" not in st.session_state:
        st.session_state.hypertension_low_BP_form_submitted = 0

    if "cvd_chd_equivalent_form_submitted" not in st.session_state:
        st.session_state.cvd_chd_equivalent_form_submitted = 0
    if "cvd_risk_factor_form_submitted" not in st.session_state:
        st.session_state.cvd_risk_factor_form_submitted = 0
    if "cvd_score_form_submitted" not in st.session_state:
        st.session_state.cvd_score_form_submitted = 0

    if "cvd_chd_equivalent_form_get_score_if_finish" not in st.session_state:
        st.session_state.cvd_chd_equivalent_form_get_score_if_finish = 0
    if "cvd_risk_factor_form_get_score_if_finish" not in st.session_state:
        st.session_state.cvd_risk_factor_form_get_score_if_finish = 0
    if "cvd_score_form_get_score_if_finish" not in st.session_state:
        st.session_state.cvd_score_form_get_score_if_finish = 0
        
    if "diabetes_risk_score_form_submitted" not in st.session_state:
        st.session_state.diabetes_risk_score_form_submitted = 0

    if "viewresult_button" not in st.session_state:
        st.session_state.viewresult_button = False
    if "back_button" not in st.session_state:
        st.session_state.back_button = False

    if "initial_screen" not in st.session_state:
        st.session_state.initial_screen = 0
