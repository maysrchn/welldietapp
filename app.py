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
        st.write("ผลการประเมินความเสี่ยงโรคเรื้อรัง")
        if st.session_state.age>=18 :
            st.subheader("======BMI======")
            st.markdown(f"BMI = {round(BMI_calculation(st.session_state.current_weight,st.session_state.height),2)}")
            st.markdown(f"BMI Class = {BMI_classification(st.session_state.current_weight,st.session_state.height)}")
            st.markdown(f"weight management plan = {str(is_must_weight_managment(st.session_state.current_weight,st.session_state.height))}")
            st.markdown("\n")
            st.subheader("======DM======")
        #     st.markdown(f"is DM =  {is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")
        #     if is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c) == False: #ไม่เป็นเบาหวาน ความเสี่ยงต้องโชว์ 
        #         st.markdown(f"Risk factor DM = {risk_factor_DM(st.session_state.weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.family_DM,st.session_state.is_HT,st.session_state.is_HT_medicinetreat,st.session_state.TG,st.session_state.HDL,st.session_state.history_GDM_Macrosomia,st.session_state.history_impaired_glucose,st.session_state.is_CVD,st.session_state.is_PCOS)}  ")
        #         st.markdown(f"Risk score DM = {risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM)}  ")
        #         if (risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM) is not None) :   #if the 'risk_score_DM' has a value
        #             st.markdown(f"ระดับความเสี่ยงต่อโรคเบาหวานใน 12 ปีข้างหน้า ของท่าน {converter_score_to_percentrisk_DM(weight,height,age,gender,waist,is_HT,family_DM)} ")
        #     else: pass  #เป็นเบาหวาน ความเสี่ยงต้องไม่โชว์ 
        #     st.markdown(Lab_fasting_DM(FBS,fastingDTX))
        #     st.markdown(f"DM Lifestyle modification = {is_must_lifestylemodification_DM(weight,height,age,gender,waist,family_DM,is_HT,is_HT_medicinetreat,TG,HDL,history_GDM_Macrosomia,history_impaired_glucose,is_CVD,is_PCOS,FBS,fastingDTX)}")
        #     st.markdown("\n")
        #     st.subheader("======HT======")
        #     st.markdown(f"HT classification = {HT_classification(SBP,DBP,age)[0]}")
        #     st.markdown(f"Risk score HT = {risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender)}")
        #     if risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender) is not None :
        #         st.markdown(f"Predict 4-year hypertension risk: {converter_score_to_percentrisk_HT(risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender))[0]}%")
        #         st.markdown(f"Risk level of HT: {converter_score_to_percentrisk_HT(risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender))[1]}")
        #     else: pass
        #     st.markdown(f"HT Lifestyle modification = {is_must_lifestylemodification_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender)}")
        #     st.markdown("\n")
        #     st.subheader("======CVD======")
        #     if age >=20:
        #         if is_CHD == False:
        #             st.markdown(f"Risk factor CVD = {risk_factor_CVD(is_smoke,SBP,DBP,is_HT_medicinetreat,HDL,family_CHD,gender,age)}")
        #             st.markdown(f"Risk score CVD = {risk_score_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD)}")
        #             if risk_score_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD) is not None :
        #                 st.markdown(f"Predict 10-year CVD risk: {converter_score_to_percentrisk_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD)}%")
        #         st.markdown(f"CVD Lifestyle modification = {is_must_lifestylemodification_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD,LDL,FBS,twoHr_postprandial,HbA1c)}")
        #     else: st.markdown(f"CVD Lifestyle modification = {is_must_lifestylemodification_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD,LDL,FBS,twoHr_postprandial,HbA1c)}")
        # else: 
        #     pass

