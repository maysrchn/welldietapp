import streamlit as st
from welldiet_assessment import *

st.title('Well Diet')
st.subheader('NCDs Risk Detection and Lifestyle Modification Therapy')
st.caption('by :blue[INVITRACE] เมย์ สรัลชนา')
 #INPUT

with st.form("my_form"):
    # Every form must have a submit button.
    gender = st.selectbox('Gender',['male','female'])
    age = st.slider('Age', 18,120)
    current_weight = st.number_input('Current Weight (kg)')
    height = st.number_input('Height (cm)',100,250)
    waist = st.number_input('Waist (inches)')
    TG = st.number_input('Triglyceride (mg/dL)')
    HDL = st.number_input('HDL (mg/dL)')
    FBS = st.number_input('FBS (mg/dL)')
    fastingDTX =st.number_input('ค่าน้ำตาลปลายนี้ว หลังอดอาหาร (mg/dL) (ถ้ามี)')
    SBP = st.number_input('Systolic Blood Pressure (mmHg)')
    DBP = st.number_input('Diastolic Blood Pressure (mmHg)')
    TC = st.number_input('Total Cholesteral (mg/dL)')
    LDL = st.number_input('LDL (mg/dL)')
    twoHr_postprandial = st.number_input('ค่าน้ำตาล หลังทานอาหาร 2 ชั่วโมง  (mg/dL) (ถ้ามี)')
    HbA1c = st.number_input('HbA1c (%) (ถ้ามี)')
    mapping = {
        "Yes": True,
        "No": False,
        "ไม่มีใครเป็น": 0,
        "เป็น 1 คน": 1,
        "เป็นทั้งพ่อทั้งแม่": 2
    }

    family_DM = st.radio(
        "มี พ่อ แม่ พี่ หรือ น้อง เป็นโรคเบาหวาน?",
        ("Yes", "No")
    )                  #มี พ่อ แม่ พี่ หรือ น้อง เป็นโรคเบาหวาน
    family_DM = mapping[family_DM]

    family_HT = st.radio(
        "มี พ่อ แม่ เป็นโรคความดันโลหิตสูง?",
        ("ไม่มีใครเป็น","เป็น 1 คน", "เป็นทั้งพ่อทั้งแม่"),
    )                           #0 คน / พ่อหรือแม่ 1 คน / ทั้งพ่อทั้งแม่ 2 คน
    family_HT = mapping[family_HT]

    family_CHD = st.radio(
        "พ่อแม่ พี่ น้อง มีโรคหัวใจ? ที่เริ่มเป็นก่อนอายุ <55 ปี(ชาย) อายุ <65 ปี(หญิง)",
        ("Yes", "No")
    )
    family_CHD = mapping[family_CHD]#พ่อแม่ พี่ น้อง มีโรค CHD ชายอายุ<55 ปี หญิง อายุ<65 ปี
    is_HT = st.radio(
        "คุณเป็นโรคความดันโลหิตสูงหรือไม่",
        ("Yes", "No")
    )
    is_HT = mapping[is_HT]                  #เป็นโรคความดันโลหิตสูงหรือไม่
    is_HT_medicinetreat = st.radio(
        "คุณกำลังรับประทานยาควบคุมความดันโลหิตสูงหรือไม่",
        ("Yes", "No")
    )
    is_HT_medicinetreat = mapping[is_HT_medicinetreat]       #กำลังรับประทานยาควบคุมความดันโลหิตสูงหรือไม่
    history_GDM_Macrosomia = st.radio(
        "มีประวัติเป็นโรคเบาหวานขณะตั้งครรภ์หรือเคยคลอดบุตรน้ำหนักเกิน",
        ("Yes", "No")
    )
    history_GDM_Macrosomia = mapping[history_GDM_Macrosomia]   #มีประวัติเป็นโรคเบาหวานขณะตั้งครรภ์หรือเคยคลอดบุตรน้ำหนักเกิน 4 กิโลกรัม

    history_impaired_glucose = st.radio(
        "เคยได้รับการตรวจพบว่าเป็น IGT หรือ IFG ?",
        ("Yes", "No")
    )
    history_impaired_glucose = mapping[history_impaired_glucose]   #เคยได้รับการตรวจพบว่าเป็น IGT หรือ IFG

    is_CVD = st.radio(
        "คุณมีโรคหัวใจและหลอดเลือด ? (cardiovascular disease)",
        ("Yes", "No")
    )
    is_CVD = mapping[is_CVD]                      #มีโรคหัวใจและหลอดเลือด (cardiovascular disease)

    is_PCOS = st.radio(
        "คุณมีกลุ่มอาการถุงน้ำในรังไข่ ? (polycystic ovarian syndrome)",
        ("Yes", "No")
    )
    is_PCOS = mapping[is_PCOS]             #มีกลุ่มอาการถุงน้ำในรังไข่ ( polycystic ovarian syndrome )

    is_smoke = st.radio("คุณสูบบุหรี่หรือไม่",("Yes", "No"))
    is_smoke = mapping[is_smoke]    #คุณสูบบุหรี่หรือไม่
    is_CHD = is_CVD                     #มีอาการ CHDไหม ให้ถือว่า CHD = CVD ATPIII ก็ไม่ต้องถามเรื่องCHD แล้ว
    weight = current_weight
    # ห้ามอายุน้อยกว่า 18
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("ผลการประเมินความเสี่ยงโรคเรื้อรัง")
    # height = float(height)
    # weight = float(weight)
    # print(round(BMI_calculation(weight,height),2))
    if age>=18 :
        st.subheader("======BMI======")
        #st.markdown(body="a",unsafe_allow_html="b")
        st.markdown(f"BMI = {round(BMI_calculation(weight,height),2)}")
        st.markdown(f"BMI Class = {BMI_classification(weight,height)}")
        st.markdown(f"weight management plan = {str(is_must_weight_managment(weight,height))}")
        st.markdown("\n")
        st.subheader("======DM======")
        st.markdown("is DM = ", is_DM(FBS,twoHr_postprandial,HbA1c))
        if is_DM(FBS,twoHr_postprandial,HbA1c) == False: #ไม่เป็นเบาหวาน ความเสี่ยงต้องโชว์ 
            st.markdown(f"Risk factor DM = {risk_factor_DM(weight,height,age,gender,waist,family_DM,is_HT,is_HT_medicinetreat,TG,HDL,history_GDM_Macrosomia,history_impaired_glucose,is_CVD,is_PCOS)}  ")
            st.markdown(f"Risk score DM = {risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM)}  ")
            if (risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM) is not None) :   #if the 'risk_score_DM' has a value
                st.markdown(f"ระดับความเสี่ยงต่อโรคเบาหวานใน 12 ปีข้างหน้า ของท่าน {converter_score_to_percentrisk_DM(weight,height,age,gender,waist,is_HT,family_DM)} ")
        else: pass  #เป็นเบาหวาน ความเสี่ยงต้องไม่โชว์ 
        st.markdown(Lab_fasting_DM(FBS,fastingDTX))
        st.markdown(f"DM Lifestyle modification = {is_must_lifestylemodification_DM(weight,height,age,gender,waist,family_DM,is_HT,is_HT_medicinetreat,TG,HDL,history_GDM_Macrosomia,history_impaired_glucose,is_CVD,is_PCOS,FBS,fastingDTX)}")
        st.markdown("\n")
        st.subheader("======HT======")
        st.markdown(f"HT classification = {HT_classification(SBP,DBP,age)[0]}")
        st.markdown(f"Risk score HT = {risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender)}")
        if risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender) is not None :
            st.markdown(f"Predict 4-year hypertension risk: {converter_score_to_percentrisk_HT(risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender))[0]}%")
            st.markdown(f"Risk level of HT: {converter_score_to_percentrisk_HT(risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender))[1]}")
        else: pass
        st.markdown(f"HT Lifestyle modification = {is_must_lifestylemodification_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender)}")
        st.markdown("\n")
        st.subheader("======CVD======")
        if age >=20:
            if is_CHD == False:
                st.markdown(f"Risk factor CVD = {risk_factor_CVD(is_smoke,SBP,DBP,is_HT_medicinetreat,HDL,family_CHD,gender,age)}")
                st.markdown(f"Risk score CVD = {risk_score_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD)}")
                if risk_score_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD) is not None :
                    st.markdown(f"Predict 10-year CVD risk: {converter_score_to_percentrisk_CVD(risk_score_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD))}%")
            st.markdown(f"CVD Lifestyle modification = {is_must_lifestylemodification_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD,LDL,FBS,twoHr_postprandial,HbA1c)}")
        else: st.markdown(f"CVD Lifestyle modification = {is_must_lifestylemodification_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD,LDL,FBS,twoHr_postprandial,HbA1c)}")
    else: 
        pass
  



    # # physical_activity="moderately active"
    # # # goal_weight=60
    # # current_food_record= 1600   #kcal



    # #cd /Users/may/Desktop/welldiet.py/ 
    # #streamlit run streamlit_welldiet.py