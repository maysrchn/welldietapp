import streamlit as st

def screener_engine():
    fullname = st.session_state['fullname']
    gender = st.session_state['gender']
    age = st.session_state['age']
    weight = st.session_state['current_weight']
    height = st.session_state['height']
    waist = st.session_state['waist']
    TG = st.session_state['TG']
    HDL = st.session_state['HDL']
    FBS = st.session_state['FBS']
    fastingDTX =st.session_state['fastingDTX']
    SBP = st.session_state['SBP']
    DBP = st.session_state['DBP']
    TC = st.session_state['TC']
    LDL = st.session_state['LDL']
    twoHr_postprandial = st.session_state['twoHr_postprandial']
    HbA1c = st.session_state['HbA1c']
    mapping = {
        "Yes": True,
        "No": False,
        "ไม่มีใครเป็น": 0,
        "เป็น 1 คน": 1,
        "เป็นทั้งพ่อทั้งแม่": 2
    }
    family_DM = st.session_state['family_DM']  #มี พ่อ แม่ พี่ หรือ น้อง เป็นโรคเบาหวาน
    family_DM = mapping[family_DM]

    family_HT = st.session_state['family_HT'] #0 คน / พ่อหรือแม่ 1 คน / ทั้งพ่อทั้งแม่ 2 คน
    family_HT = mapping[family_HT]

    family_CHD = st.session_state['family_CHD']
    family_CHD = mapping[family_CHD]#พ่อแม่ พี่ น้อง มีโรค CHD ชายอายุ<55 ปี หญิง อายุ<65 ปี
    is_HT = st.session_state['is_HT']
    is_HT = mapping[is_HT]                  #เป็นโรคความดันโลหิตสูงหรือไม่
    is_HT_medicinetreat = st.session_state['is_HT_medicinetreat']
    is_HT_medicinetreat = mapping[is_HT_medicinetreat]       #กำลังรับประทานยาควบคุมความดันโลหิตสูงหรือไม่
    history_GDM_Macrosomia = st.session_state['history_GDM_Macrosomia']
    history_GDM_Macrosomia = mapping[history_GDM_Macrosomia]   #มีประวัติเป็นโรคเบาหวานขณะตั้งครรภ์หรือเคยคลอดบุตรน้ำหนักเกิน 4 กิโลกรัม

    history_impaired_glucose = st.session_state['history_impaired_glucose']
    history_impaired_glucose = mapping[history_impaired_glucose]   #เคยได้รับการตรวจพบว่าเป็น IGT หรือ IFG

    is_CVD = st.session_state['is_CVD']
    is_CVD = mapping[is_CVD]                      #มีโรคหัวใจและหลอดเลือด (cardiovascular disease)

    is_PCOS = st.session_state['is_PCOS']
    is_PCOS = mapping[is_PCOS]             #มีกลุ่มอาการถุงน้ำในรังไข่ ( polycystic ovarian syndrome )

    is_smoke = st.session_state['is_smoke']
    is_smoke = mapping[is_smoke]    #คุณสูบบุหรี่หรือไม่
    is_CHD = is_CVD                     #มีอาการ CHDไหม ให้ถือว่า CHD = CVD ATPIII ก็ไม่ต้องถามเรื่องCHD แล้ว
    # weight = current_weight


