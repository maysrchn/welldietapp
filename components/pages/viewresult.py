import streamlit as st
from RiskEngine.RiskEngine import*
from RiskEngine.welldiet_weightloss_program import weight_loss_module
from RiskEngine.welldiet_weightgain_program import weight_gain_module
def viewresult():
    col1,col2 = st.columns([0.2,0.8])
    with col1:
        st.markdown(st.session_state['fullname'])
        st.markdown(f"เพศ {st.session_state['gender']}")
        st.markdown(f"อายุ {st.session_state['age']}")
        st.markdown(f"น้ำหนัก {st.session_state['current_weight']}")
        st.markdown(f"ส่วนสูง {st.session_state['height']}")
    with col2:
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        with col1:
            st.markdown("พลังงานที่ใช้ไปใน 1 วัน (TDEE)")
            st.subheader(f":red[{weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[0]}]")
            st.markdown("kcal")
        with col2:
            st.markdown("พลังงานพื้นฐานที่ร่างกายจำเป็นต้องได้รับในแต่ละวัน (BMR)")
            st.subheader(f"{weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[1]}")
            st.markdown("kcal")
        st.subheader(":red[ผลการประเมินความเสี่ยงโรคเรื้อรัง]")
        col1, col2, col3 ,col4= st.columns(4)
        with col1:
            st.subheader("BMI")
            st.markdown(f"BMI = {round(BMI_calculation(st.session_state.current_weight,st.session_state.height),2)} kg/sqm")
            st.markdown(f"BMI Class = {BMI_classification(st.session_state.current_weight,st.session_state.height)}")
            st.markdown(f"weight management plan = {str(is_must_weight_managment(st.session_state.current_weight,st.session_state.height))}")            

        with col2:
            st.subheader("HT")
            st.markdown(f"ระดับความดันโลหิต อยู่ในเกณฑ์ = {HT_classification(st.session_state.SBP,st.session_state.DBP,st.session_state.age)[0]}")
            st.markdown(f"คะแนนความเสี่ยงภาวะความดันโลหิตสูง = {risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender)}")
            if risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender) is not None :
                st.markdown(f"ระดับความเสี่ยงต่อภาวะความดันโลหิตสูง ในอีก 4 ปีข้างหน้า = {converter_score_to_percentrisk_HT(risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender))[0]}%")
                st.markdown(f"ความเสี่ยงจัดอยู่ในกลุ่ม = {converter_score_to_percentrisk_HT(risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender))[1]}")
            else: pass
            st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมความดันโลหิตสูง = {is_must_lifestylemodification_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender)}")
            
        with col3:
            st.subheader("CVD")
            if st.session_state.age >=20:
                if st.session_state.is_CVD == False:
                    st.markdown(f"จำนวนปัจจัยเสี่ยงโรคหลอดเลือดหัวใจ= {risk_factor_CVD(st.session_state.is_smoke,st.session_state.SBP,st.session_state.DBP,st.session_state.is_HT_medicinetreat,st.session_state.HDL,st.session_state.family_CHD,st.session_state.gender,st.session_state.age)}")
                    st.markdown(f"คะแนนความเสี่ยงโรคหลอดเลือดหัวใจ = {risk_score_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD)}")
                    if risk_score_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD) is not None :
                        st.markdown(f"ระดับความเสี่ยงโรคหลอดเลือดหัวใจ ในอีก 10 ปีข้างหน้า = {converter_score_to_percentrisk_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD)}%")
                st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมโรคหลอดเลือดหัวใจ = {is_must_lifestylemodification_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD,st.session_state.LDL,st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")
            else: st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมโรคหลอดเลือดหัวใจ = {is_must_lifestylemodification_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD,st.session_state.LDL,st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")

        with col4:
            st.subheader("DM")
            st.markdown(f"เข้าข่ายถูกวินิจฉัยเบาหวานหรือไม่ =  {is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")
            if is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c) == False: #ไม่เป็นเบาหวาน ความเสี่ยงต้องโชว์ 
                st.markdown(f"คะแนนความเสี่ยงเบาหวาน (0 - 17) = {risk_score_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.is_HT,st.session_state.family_DM)}  ")
                if (risk_score_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.is_HT,st.session_state.family_DM) is not None) :   #if the 'risk_score_DM' has a value
                    st.markdown(f"ระดับความเสี่ยงต่อโรคเบาหวานใน 12 ปีข้างหน้า = {converter_score_to_percentrisk_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.is_HT,st.session_state.family_DM)} ")
            else: pass  #เป็นเบาหวาน ความเสี่ยงต้องไม่โชว์ 
            st.markdown(Lab_fasting_DM(st.session_state.FBS,st.session_state.fastingDTX))
            st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมเบาหวาน = {is_must_lifestylemodification_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.family_DM,st.session_state.is_HT,st.session_state.FBS,st.session_state.fastingDTX)}")
        st.subheader(":red[คำแนะนำ]")
        col1, col2, col3 ,col4= st.columns(4)
        with col1:
            if st.session_state.goal_weight < st.session_state.current_weight :
                st.subheader(weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[2])
                st.markdown(weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[3])
                st.markdown(weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[4])
                st.markdown(weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[5])
                st.markdown(weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[6])
                st.markdown(weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[7])
                st.markdown(weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[8])
            
            else:
                st.subheader(weight_gain_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[2])
                st.markdown(weight_gain_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[3])
                st.markdown(weight_gain_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[4])
                st.markdown(weight_gain_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[5])
                st.markdown(weight_gain_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[6])
                st.markdown(weight_gain_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[7])
                st.markdown(weight_gain_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)[8])

        with col2:
            st.subheader(is_must_lifestylemodification_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.family_DM,st.session_state.is_HT,st.session_state.FBS,st.session_state.fastingDTX))
        with col3:
            st.subheader(is_must_lifestylemodification_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD,st.session_state.LDL,st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c))
        with col4:
            st.subheader(is_must_lifestylemodification_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender))



        

        # st.subheader("ผลการประเมินความเสี่ยงโรคเรื้อรัง")
        #     st.subheader("======BMI======")
        #     st.markdown(f"BMI = {round(BMI_calculation(st.session_state.current_weight,st.session_state.height),2)}")
        #     st.markdown(f"BMI Class = {BMI_classification(st.session_state.current_weight,st.session_state.height)}")
        #     st.markdown(f"weight management plan = {str(is_must_weight_managment(st.session_state.current_weight,st.session_state.height))}")
        #     st.markdown("\n")
        #     st.subheader("======DM======")
        #     st.markdown(f"เข้าข่ายถูกวินิจฉัยเบาหวานหรือไม่ =  {is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")
        #     if is_DM(st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c) == False: #ไม่เป็นเบาหวาน ความเสี่ยงต้องโชว์ 
        #         st.markdown(f"คะแนนความเสี่ยงเบาหวาน (0 - 17) = {risk_score_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.is_HT,st.session_state.family_DM)}  ")
        #         if (risk_score_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.is_HT,st.session_state.family_DM) is not None) :   #if the 'risk_score_DM' has a value
        #             st.markdown(f"ระดับความเสี่ยงต่อโรคเบาหวานใน 12 ปีข้างหน้า = {converter_score_to_percentrisk_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.is_HT,st.session_state.family_DM)} ")
        #     else: pass  #เป็นเบาหวาน ความเสี่ยงต้องไม่โชว์ 
        #     st.markdown(Lab_fasting_DM(st.session_state.FBS,st.session_state.fastingDTX))
        #     st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมเบาหวาน = {is_must_lifestylemodification_DM(st.session_state.current_weight,st.session_state.height,st.session_state.age,st.session_state.gender,st.session_state.waist,st.session_state.family_DM,st.session_state.is_HT,st.session_state.FBS,st.session_state.fastingDTX)}")
        #     st.markdown("\n")
        #     st.subheader("======HT======")
        #     st.markdown(f"ระดับความดันโลหิต อยู่ในเกณฑ์ = {HT_classification(st.session_state.SBP,st.session_state.DBP,st.session_state.age)[0]}")
        #     st.markdown(f"คะแนนความเสี่ยงภาวะความดันโลหิตสูง = {risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender)}")
        #     if risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender) is not None :
        #         st.markdown(f"ระดับความเสี่ยงต่อภาวะความดันโลหิตสูง ในอีก 4 ปีข้างหน้า = {converter_score_to_percentrisk_HT(risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender))[0]}%")
        #         st.markdown(f"ความเสี่ยงจัดอยู่ในกลุ่ม = {converter_score_to_percentrisk_HT(risk_score_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender))[1]}")
        #     else: pass
        #     st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมความดันโลหิตสูง = {is_must_lifestylemodification_HT(st.session_state.SBP,st.session_state.DBP,st.session_state.age,st.session_state.current_weight,st.session_state.height,st.session_state.is_smoke,st.session_state.family_HT,st.session_state.gender)}")
        #     st.markdown("\n")
        #     st.subheader("======CVD======")
        #     if st.session_state.age >=20:
        #         if st.session_state.is_CVD == False:
        #             st.markdown(f"จำนวนปัจจัยเสี่ยงโรคหลอดเลือดหัวใจ= {risk_factor_CVD(st.session_state.is_smoke,st.session_state.SBP,st.session_state.DBP,st.session_state.is_HT_medicinetreat,st.session_state.HDL,st.session_state.family_CHD,st.session_state.gender,st.session_state.age)}")
        #             st.markdown(f"คะแนนความเสี่ยงโรคหลอดเลือดหัวใจ = {risk_score_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD)}")
        #             if risk_score_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD) is not None :
        #                 st.markdown(f"ระดับความเสี่ยงโรคหลอดเลือดหัวใจ ในอีก 10 ปีข้างหน้า = {converter_score_to_percentrisk_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD)}%")
        #         st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมโรคหลอดเลือดหัวใจ = {is_must_lifestylemodification_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD,st.session_state.LDL,st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")
        #     else: st.markdown(f"การปรับวิถีชีวิตเพื่อควบคุมโรคหลอดเลือดหัวใจ = {is_must_lifestylemodification_CVD(st.session_state.age,st.session_state.gender,st.session_state.is_CVD,st.session_state.TC,st.session_state.is_smoke,st.session_state.HDL,st.session_state.is_HT_medicinetreat,st.session_state.SBP,st.session_state.DBP,st.session_state.family_CHD,st.session_state.LDL,st.session_state.FBS,st.session_state.twoHr_postprandial,st.session_state.HbA1c)}")
        #     if st.session_state.goal_weight < st.session_state.current_weight :
        #         weight_loss_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)
        #     else : weight_gain_module(st.session_state.age, st.session_state.gender, st.session_state.height, st.session_state.current_weight, st.session_state.physical_activity, st.session_state.goal_weight,st.session_state.current_food_record)
