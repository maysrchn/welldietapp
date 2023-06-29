import streamlit as st
st.title('Well Diet')
st.subheader('NCDs Risk Detection and Lifestyle Modification Therapy')
st.caption('by :blue[INVITRACE] เมย์ สรัลชนา')
 #INPUT
gender = st.selectbox('Gender',['Male','Female'])
age = st.slider('Age', 18,120)
current_weight = st.number_input('Current Weight (kg)')
height = st.number_input('Height (cm)')
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
# family_CHD = False                   #พ่อแม่ พี่ น้อง มีโรค CHD ชายอายุ<55 ปี หญิง อายุ<65 ปี
# is_HT = False                       #เป็นโรคความดันโลหิตสูงหรือไม่
# is_HT_medicinetreat = False         #กำลังรับประทานยาควบคุมความดันโลหิตสูงหรือไม่
# history_GDM_Macrosomia =False       #มีประวัติเป็นโรคเบาหวานขณะตั้งครรภ์หรือเคยคลอดบุตรน้ำหนักเกิน 4 กิโลกรัม
# history_impaired_glucose = False    #เคยได้รับการตรวจพบว่าเป็น IGT หรือ IFG
# is_CVD = False                     #มีโรคหัวใจและหลอดเลือด (cardiovascular disease)
# is_PCOS = False                     #มีกลุ่มอาการถุงน้ำในรังไข่ ( polycystic ovarian syndrome )
# is_smoke = False                     #คุณสูบบุหรี่หรือไม่
# is_CHD = is_CVD                     #มีอาการ CHDไหม ให้ถือว่า CHD = CVD ATPIII ก็ไม่ต้องถามเรื่องCHD แล้ว
# # # ห้ามอายุน้อยกว่า 18

# physical_activity="moderately active"
# goal_weight=60
# current_food_record= 1600   #kcal

st.button('Click')

#cd /Users/may/Desktop/welldiet.py/ 
#streamlit run streamlit_welldiet.py