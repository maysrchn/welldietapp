import streamlit as st
#INPUT
gender = "female"
age = 29
current_weight = 70
height = 163
waist = 27.5
TG = 100
HDL = 50
FBS = 90
fastingDTX = 0                      #ถ้ามี
SBP = 92
DBP = 53
TC = 100
LDL = 98
twoHr_postprandial = 0              #ถ้ามี
HbA1c = 0                           #ถ้ามี
family_DM = False                   #มี พ่อ แม่ พี่ หรือ น้อง เป็นโรคเบาหวาน
family_HT = 1                       #0 คน / พ่อหรือแม่ 1 คน / ทั้งพ่อทั้งแม่ 2 คน
family_CHD = False                   #พ่อแม่ พี่ น้อง มีโรค CHD ชายอายุ<55 ปี หญิง อายุ<65 ปี
is_HT = False                       #เป็นโรคความดันโลหิตสูงหรือไม่
is_HT_medicinetreat = False         #กำลังรับประทานยาควบคุมความดันโลหิตสูงหรือไม่
history_GDM_Macrosomia =False       #มีประวัติเป็นโรคเบาหวานขณะตั้งครรภ์หรือเคยคลอดบุตรน้ำหนักเกิน 4 กิโลกรัม
history_impaired_glucose = False    #เคยได้รับการตรวจพบว่าเป็น IGT หรือ IFG
is_CVD = False                     #มีโรคหัวใจและหลอดเลือด (cardiovascular disease)
is_PCOS = False                     #มีกลุ่มอาการถุงน้ำในรังไข่ ( polycystic ovarian syndrome )
is_smoke = False                     #คุณสูบบุหรี่หรือไม่
is_CHD = is_CVD                     #มีอาการ CHDไหม ให้ถือว่า CHD = CVD ATPIII ก็ไม่ต้องถามเรื่องCHD แล้ว
# ห้ามอายุน้อยกว่า 18

physical_activity="moderately active"
goal_weight=60
current_food_record= 1600   #kcal