import streamlit as st
from components.state.state import initialize_state
# from components.screener.screener import screener_engine
from RiskEngine.RiskEngine import*
from components.pages.navigator_tab import streamlit_menu
initialize_state()
from components.pages.demographic_profile import demographic_form
from components.pages.bmi import bmi_form
from components.pages.weight_management import weightcontrol_form
from components.pages.ht_screener import HypertensionScreener
from components.pages.cvd_screener import CVDScreener
from components.pages.diabetes import diabetes_risk_score_form


#make it look nice from the start
st.set_page_config(layout='wide')

st.title('Well Diet')
st.subheader('NCDs Risk Detection and Lifestyle Modification Therapy')
st.caption('by :blue[INVITRACE] เมย์ สรัลชนา')


# screener_engine()
st.session_state.streamlit_menu = streamlit_menu()

col1,col2 = st.columns([2,1])

with col1:
    #ถ้าเปิดหน้าโปรไฟล
    if st.session_state.streamlit_menu == "Profile":
        demographic_form()
    elif st.session_state.streamlit_menu == "BMI":
        bmi_form()
    elif st.session_state.streamlit_menu == "Weight Control":
        weightcontrol_form()
    elif st.session_state.streamlit_menu == "Hypertension":
        HypertensionScreener()
    elif st.session_state.streamlit_menu == "Cardiovascular":
        CVDScreener()
    elif st.session_state.streamlit_menu == "Diabetes":
        diabetes_risk_score_form()

with col2: 
    st.subheader("Completion")
    if st.session_state.profile_form_submitted> 0 :
        st.success("Profile",  icon= "✅")
    else: st.info("Profile")
    if st.session_state.bmi_form_submitted > 0 :
        st.success("BMI",  icon= "✅")
    else: st.info("BMI")
    if st.session_state.weightcontrol_form_submitted > 0 :
        st.success("Weight Control",  icon= "✅")        
    else: st.info("Weight Control")
    if st.session_state.hypertension_BP_form_submitted or st.session_state.hypertension_low_BP_form_submitted >0 :
        st.success("Hypertension",  icon= "✅")        
    else: st.info("Hypertension")
    if (st.session_state.cvd_chd_equivalent_form_get_score_if_finish or st.session_state.cvd_risk_factor_form_get_score_if_finish or st.session_state.cvd_score_form_get_score_if_finish)>0 :
        st.success("Cardiovascular",  icon= "✅")        
    else: st.info("Cardiovascular")
    if st.session_state.diabetes_risk_score_form_submitted > 0 :
        st.success("Diabetes",  icon= "✅")
    else: st.info("Diabetes")
    viewresult=st.button("View Result")
if viewresult:
    st.subheader("ผลการประเมินความเสี่ยงโรคเรื้อรัง")
    st.markdown(st.session_state['fullname'])
    st.markdown(f"เพศ {st.session_state['gender']}")
    st.markdown(f"อายุ {st.session_state['age']}")
    if st.session_state.age>=18 :
        st.subheader("======BMI======")
        st.markdown(f"BMI = {round(BMI_calculation(st.session_state.current_weight,st.session_state.height),2)}")
        st.markdown(f"BMI Class = {BMI_classification(st.session_state.current_weight,st.session_state.height)}")
        st.markdown(f"weight management plan = {str(is_must_weight_managment(st.session_state.current_weight,st.session_state.height))}")
        st.markdown("\n")
        st.subheader("======DM======")
        st.markdown(f"เข้าข่ายถูกวินิจฉัยเบาหวานหรือไม่ =  {is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")
        if is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c) == False: #ไม่เป็นเบาหวาน ความเสี่ยงต้องโชว์ 
            st.markdown(f"คะแนนความเสี่ยงเบาหวาน (0 - 17) = {risk_score_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.is_HT,st.session_state.family_DM)}  ")
            if (risk_score_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.is_HT,st.session_state.family_DM) is not None) :   #if the 'risk_score_DM' has a value
                st.markdown(f"ระดับความเสี่ยงต่อโรคเบาหวานใน 12 ปีข้างหน้า = {converter_score_to_percentrisk_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.is_HT,st.session_state.family_DM)} ")
        else: pass  #เป็นเบาหวาน ความเสี่ยงต้องไม่โชว์ 
        st.markdown(Lab_fasting_DM(st.session_state.FBS,st.session_state.fastingDTX))
        st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมเบาหวาน = {is_must_lifestylemodification_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.family_DM,st.session_state.is_HT,st.session_state.FBS,st.session_state.fastingDTX)}")
        st.markdown("\n")
        st.subheader("======HT======")
        st.markdown(f"ระดับความดันโลหิต อยู่ในเกณฑ์ = {HT_classification(st.session_state.SBP,st.session_state.DBP,st.session_state.age)[0]}")
        st.markdown(f"คะแนนความเสี่ยงภาวะความดันโลหิตสูง = {risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender)}")
        if risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender) is not None :
            st.markdown(f"ระดับความเสี่ยงต่อภาวะความดันโลหิตสูง ในอีก 4 ปีข้างหน้า = {converter_score_to_percentrisk_HT(risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender))[0]}%")
            st.markdown(f"ความเสี่ยงจัดอยู่ในกลุ่ม = {converter_score_to_percentrisk_HT(risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender))[1]}")
        else: pass
        st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมความดันโลหิตสูง = {is_must_lifestylemodification_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender)}")
        st.markdown("\n")
        st.subheader("======CVD======")
        if st.session_state.age >=20:
            if st.session_state.is_CVD == False:
                st.markdown(f"จำนวนปัจจัยเสี่ยงโรคหลอดเลือดหัวใจ= {risk_factor_CVD(st.session_state.is_smoke,st.session_state.SBP,st.session_state.DBP,st.session_state.is_HT_medicinetreat,st.session_state.HDL,st.session_state.family_CHD,st.session_state.gender,st.session_state.age)}")
                st.markdown(f"คะแนนความเสี่ยงโรคหลอดเลือดหัวใจ = {risk_score_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD)}")
                if risk_score_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD) is not None :
                    st.markdown(f"ระดับความเสี่ยงโรคหลอดเลือดหัวใจ ในอีก 10 ปีข้างหน้า = {converter_score_to_percentrisk_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD)}%")
            st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมโรคหลอดเลือดหัวใจ = {is_must_lifestylemodification_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD,st.session_state.LDL,st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")
        else: st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมโรคหลอดเลือดหัวใจ = {is_must_lifestylemodification_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD,st.session_state.LDL,st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")
    else: 
        pass

