#current_weight = 10
#weight = current_weight
# True = abnormal
def waist_calculation (gender,waist):
    if gender == "female" and waist >= 32 :
        return True
    elif gender == "male" and waist >= 36 :
        return True
    return False

def BMI_calculation (weight,height) :
    BMI = weight/(height*0.01)**2
    return BMI

def is_DM(FBS,twoHr_postprandial,HbA1c):
    if FBS >= 126 or twoHr_postprandial >=200 or HbA1c >=6.5:
        return True
    else : return False

#Obesity
def BMI_classification (weight,height):
    if BMI_calculation (weight,height) < 18.5 :
        BMI_class = "Underweight"
    elif 18.5 <= BMI_calculation (weight,height) <23 :
        BMI_class = "Normal BMI"
    elif 23 <= BMI_calculation (weight,height) <25 :
        BMI_class = "Overweight"
    elif 25 <= BMI_calculation (weight,height) <30 :
        BMI_class = "Obesity class I"
    elif BMI_calculation (weight,height) >=30 :
        BMI_class = "Obesity class II"
    return BMI_class

def is_must_weight_managment(weight,height):
    if BMI_calculation (weight,height) >=23:
        return "Caloric Restriction"
    if 18.5 <= BMI_calculation (weight,height) <23 :
        return "Stay Healthy Diet"
    if BMI_calculation (weight,height) < 18.5 :
        return "Caloric Boost Up"
#Diabetes
#risk more than 1 from 8
def risk_factor_DM(weight,height,age,gender,waist,family_DM,is_HT,is_HT_medicinetreat,TG,HDL,history_GDM_Macrosomia,history_impaired_glucose,is_CVD,is_PCOS):
    if age <18 :
        risk_count = None
    elif age >=18:
        risk_count = 0

        if age >= 35:
            risk_count += 1
        
        if (BMI_calculation (weight,height) >= 25 or waist_calculation(gender, waist)) and family_DM:
            risk_count += 1

        if is_HT == True or is_HT_medicinetreat == True:
            risk_count += 1
        
        if TG > 250 or HDL < 35:
            risk_count += 1
        
        if history_GDM_Macrosomia == True:
            risk_count += 1
        
        if history_impaired_glucose == True:
            risk_count += 1
        
        if is_CVD == True:
            risk_count += 1

        if is_PCOS == True:
            risk_count += 1

    return risk_count

#DM risk score

def risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM):
    if age <34 :
        risk_score_DM_sum = None
    elif age >=34:
        risk_score_DM_sum = 0
        if 34 <= age < 45 :
            risk_score_DM_sum += 0
        elif 45 <= age < 50 :
            risk_score_DM_sum += 1
        elif age >= 50 :
            risk_score_DM_sum += 2
        
        if  gender == "female" :
            risk_score_DM_sum += 0
        elif gender == "male" :
            risk_score_DM_sum += 2

        if  BMI_calculation (weight,height) < 23 :
            risk_score_DM_sum += 0
        elif 23 >= BMI_calculation (weight,height) < 27.5 :    
            risk_score_DM_sum += 3
        elif BMI_calculation (weight,height) >= 27.5 :    
            risk_score_DM_sum += 5

        if waist_calculation (gender,waist) == False :
            risk_score_DM_sum += 0
        elif waist_calculation (gender,waist) == True :
            risk_score_DM_sum += 2

        if is_HT == False :
            risk_score_DM_sum += 0
        elif is_HT == True :
            risk_score_DM_sum += 2

        if family_DM == False :
            risk_score_DM_sum += 0
        elif family_DM == True :
            risk_score_DM_sum += 4

    return risk_score_DM_sum 



#DM Lab result Fasting
def Lab_fasting_DM(FBS,fastingDTX):
    lab_DM = ""
    if FBS >= 100 or fastingDTX >= 100 :
        lab_DM = "lab DM abnormal"
    else : lab_DM = "lab DM normal"
    return lab_DM

def converter_score_to_percentrisk_DM(weight,height,age,gender,waist,is_HT,family_DM):
    if 0 <= risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM) < 3 :
        percentrisk_DM = "น้อยกว่า 5%"
    elif 3 <= risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM) < 6 :
        percentrisk_DM = "เท่ากับ 5% - 10%"
    elif 6 <= risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM) <= 8 :
        percentrisk_DM = "เท่ากับ 11% - 20%"
    elif risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM) > 8 :
        percentrisk_DM = "มากกว่า 11% - 20%"
    return percentrisk_DM

def is_must_lifestylemodification_DM(weight,height,age,gender,waist,family_DM,is_HT,is_HT_medicinetreat,TG,HDL,history_GDM_Macrosomia,history_impaired_glucose,is_CVD,is_PCOS,FBS,fastingDTX):
    if age>=34 :
        if risk_factor_DM(weight,height,age,gender,waist,family_DM,is_HT,is_HT_medicinetreat,TG,HDL,history_GDM_Macrosomia,history_impaired_glucose,is_CVD,is_PCOS) > 0 or risk_score_DM(weight,height,age,gender,waist,is_HT,family_DM) >= 6 or Lab_fasting_DM(FBS,fastingDTX) == "lab DM abnormal":
            return "must"
        else : return "don't need to"
    if age < 34 :
        if risk_factor_DM(weight,height,age,gender,waist,family_DM,is_HT,is_HT_medicinetreat,TG,HDL,history_GDM_Macrosomia,history_impaired_glucose,is_CVD,is_PCOS) > 0 or Lab_fasting_DM(FBS,fastingDTX) == "lab DM abnormal":
            return "must"
        else : return "don't need to"



#Hypertension

def HT_classification(SBP,DBP,age):
    if age >= 18 :
        SBP_score = 0
        if SBP < 130:
            SBP_score += 1
        elif 130 <= SBP < 140:
            SBP_score += 2
        elif 140 <= SBP < 160:
            SBP_score += 3
        elif 160 <= SBP < 180:
            SBP_score += 4
        elif SBP >= 180:
            SBP_score += 5

        DBP_score = 0
        if DBP < 85:
            DBP_score += 1
        elif 85 <= DBP < 90:
            DBP_score += 2
        elif 90 <= DBP < 100:
            DBP_score += 3
        elif 100 <= DBP < 110:
            DBP_score += 4
        elif DBP >= 110:
            DBP_score += 5

        BP_score_final = max(SBP_score, DBP_score)

        if BP_score_final == 1:
            DiagBP = "Normal"
        elif BP_score_final == 2:
            DiagBP = "High Normal"
        elif BP_score_final == 3:
            DiagBP = "Hypertension Stage 1"
        elif BP_score_final == 4:
            DiagBP = "Hypertension Stage 2"
        elif BP_score_final == 5:
            DiagBP = "Hypertension Stage 3"

        result_BP = [DiagBP,BP_score_final]
        return result_BP
    else : pass

def risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender):
    risk_score_HT_sum = None
    if HT_classification(SBP,DBP,age) == None or age <20 or age >80:
        pass
    elif HT_classification(SBP,DBP,age)[1]<3 and 20 <=age <=80 :
        risk_score_HT_sum = 0
        if  gender == "female" :
            risk_score_HT_sum += 1
        elif gender == "male" :
            risk_score_HT_sum += 0

        if  BMI_calculation(weight,height) < 25 :
            risk_score_HT_sum += 0
        elif 25 >= BMI_calculation(weight,height) <= 30 :    
            risk_score_HT_sum += 3
        elif BMI_calculation(weight,height) > 30 :    
            risk_score_HT_sum += 5

        if  SBP < 110 :
            risk_score_HT_sum += -4
        elif 110 <= SBP < 115 :    
            risk_score_HT_sum += 0
        elif 115 <= SBP < 120 :    
            risk_score_HT_sum += 2
        elif 120 <= SBP < 125 :    
            risk_score_HT_sum += 4
        elif 125 <= SBP < 130 :    
            risk_score_HT_sum += 6
        elif 130 <= SBP < 135 :    
            risk_score_HT_sum += 8
        elif 135 <= SBP < 140 :    
            risk_score_HT_sum += 10
        
        if 20 <= age < 30 :
            if DBP < 70 :
                risk_score_HT_sum += -8
            elif 70 <= DBP < 75 :    
                risk_score_HT_sum += -3
            elif 75 <= DBP < 80 :    
                risk_score_HT_sum += 2
            elif 80 <= DBP < 85 :    
                risk_score_HT_sum += 4
            elif 85 <= DBP < 90 :    
                risk_score_HT_sum += 6

        if 30 <= age < 40 :
            if DBP < 70 :
                risk_score_HT_sum += -5
            elif 70 <= DBP < 75 :    
                risk_score_HT_sum += 0
            elif 75 <= DBP < 80 :    
                risk_score_HT_sum += 2
            elif 80 <= DBP < 85 :    
                risk_score_HT_sum += 5
            elif 85 <= DBP < 90 :    
                risk_score_HT_sum += 7

        if 40 <= age < 50 :
            if DBP < 70 :
                risk_score_HT_sum += -1
            elif 70 <= DBP < 75 :    
                risk_score_HT_sum += 3
            elif 75 <= DBP < 80 :    
                risk_score_HT_sum += 5
            elif 80 <= DBP < 85 :    
                risk_score_HT_sum += 6
            elif 85 <= DBP < 90 :    
                risk_score_HT_sum += 8

        if 50 <= age < 60 :
            if DBP < 70 :
                risk_score_HT_sum += 3
            elif 70 <= DBP < 75 :    
                risk_score_HT_sum += 5
            elif 75 <= DBP < 80 :    
                risk_score_HT_sum += 7
            elif 80 <= DBP < 85 :    
                risk_score_HT_sum += 8
            elif 85 <= DBP < 90 :    
                risk_score_HT_sum += 9

        if 60 <= age < 70 :
            if DBP < 70 :
                risk_score_HT_sum += 6
            elif 70 <= DBP < 75 :    
                risk_score_HT_sum += 8
            elif 75 <= DBP < 80 :    
                risk_score_HT_sum += 9
            elif 80 <= DBP < 85 :    
                risk_score_HT_sum += 10
            elif 85 <= DBP < 90 :    
                risk_score_HT_sum += 10

        if 70 <= age < 80 :
            if DBP < 70 :
                risk_score_HT_sum += 10
            elif 70 <= DBP < 75 :    
                risk_score_HT_sum += 11
            elif 75 <= DBP < 80 :    
                risk_score_HT_sum += 11
            elif 80 <= DBP < 85 :    
                risk_score_HT_sum += 11
            elif 85 <= DBP < 90 :    
                risk_score_HT_sum += 11

        if  is_smoke == True :
            risk_score_HT_sum += 1
        elif is_smoke == False :
            risk_score_HT_sum += 0

        if family_HT == 0 :
            risk_score_HT_sum += 0
        elif family_HT == 1 :
            risk_score_HT_sum += 1
        elif family_HT == 2 :
            risk_score_HT_sum += 2
    return risk_score_HT_sum



def converter_score_to_percentrisk_HT(risk_score_HT_sum):
    mappings = {
        -12: (0.22, "Low risk"),
        -11: (0.27, "Low risk"),
        -10: (0.31, "Low risk"),
        -9: (0.37, "Low risk"),
        -8: (0.44, "Low risk"),
        -7: (0.52, "Low risk"),
        -6: (0.62, "Low risk"),
        -5: (0.73, "Low risk"),
        -4: (0.86, "Low risk"),
        -3: (1.02, "Low risk"),
        -2: (1.21, "Low risk"),
        -1: (1.43, "Low risk"),
        0: (1.69, "Low risk"),
        1: (2.0, "Low risk"),
        2: (2.37, "Low risk"),
        3: (2.8, "Low risk"),
        4: (3.31, "Low risk"),
        5: (3.9, "Low risk"),
        6: (4.61, "Low risk"),
        7: (5.43, "Medium risk"),
        8: (6.4, "Medium risk"),
        9: (7.53, "Medium risk"),
        10: (8.86, "Medium risk"),
        11: (10.4, "High risk"),
        12: (12.2, "High risk"),
        13: (14.28, "High risk"),
        14: (16.68, "High risk"),
        15: (19.43, "High risk"),
        16: (22.58, "High risk"),
        17: (26.14, "High risk"),
        18: (30.16, "High risk"),
        19: (34.63, "High risk"),
        20: (39.55, "High risk"),
        21: (44.91, "High risk"),
        22: (50.64, "High risk"),
        23: (56.66, "High risk"),
        24: (62.85, "High risk"),
        25: (69.05, "High risk"),
        26: (75.06, "High risk"),
        27: (80.69, "High risk"),
        28: (85.74, "High risk")
    }
    if risk_score_HT_sum in mappings:
        return mappings[risk_score_HT_sum]
    else:
        raise ValueError("Invalid SUM Score")


def is_must_lifestylemodification_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender):
    if risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender) is not None:
        if risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender) > 10 or  HT_classification(SBP,DBP,age)[1] >= 3 :
            return "must "
        else : return "don't need to "
    elif (risk_score_HT(SBP,DBP,age,weight,height,is_smoke,family_HT,gender) is None) and (HT_classification(SBP,DBP,age)[1] >= 3):
        return "must "
    else :
        return "don't need to "

print("\n")
#Cardiovascular disease

def risk_factor_CVD(is_smoke,SBP,DBP,is_HT_medicinetreat,HDL,family_CHD,gender,age):
    risk_count = 0
    if is_smoke is True:
        risk_count += 1
    if age >=18 :
        if HT_classification(SBP,DBP,age)[1]>=3 or is_HT_medicinetreat == True :
            risk_count += 1
    else : pass

    if  HDL < 40:
        risk_count += 1

    if HDL >= 60 :
        risk_count += -1

    if  family_CHD is True :
        risk_count += 1

    if gender == "male" and age >= 45:
        risk_count += 1
    elif gender == "female" and age >= 55:
        risk_count += 1

    return risk_count
    
    

def risk_score_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD) : #Framimgham point score
    if 20 <= age <80 and (risk_factor_CVD(is_smoke,SBP,DBP,is_HT_medicinetreat,HDL,family_CHD,gender,age) >= 2 or is_CHD == True):
        risk_score_CVD_sum = 0
        if gender == "male" :
            if 20 <= age < 35 :
                risk_score_CVD_sum += -9
            elif 35 <= age < 40 :
                risk_score_CVD_sum += -4
            elif 40 <= age < 45 :
                risk_score_CVD_sum += 0
            elif 45 <= age < 50 :
                risk_score_CVD_sum += 3
            elif 50 <= age < 55 :
                risk_score_CVD_sum += 6
            elif 55 <= age < 60 :
                risk_score_CVD_sum += 8
            elif 60 <= age < 65 :
                risk_score_CVD_sum += 10
            elif 65 <= age < 70 :
                risk_score_CVD_sum += 11
            elif 70 <= age < 75 :
                risk_score_CVD_sum += 12
            elif 75 <= age < 80 :
                risk_score_CVD_sum += 13
            if TC < 160 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 0
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 0
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 0
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 0
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 0
            elif 160 <= TC < 200 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 4
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 3
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 2
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 1
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 0
            elif 200 <= TC < 240 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 7
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 5
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 3
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 1
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 0
            elif 240 <= TC < 280 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 9
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 6
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 4
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 2
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 1
            elif  TC >= 280 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 11
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 8
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 5
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 3
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 1
            if is_smoke == False :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 0
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 0
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 0
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 0
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 0
            elif is_smoke == True :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 8
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 5
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 3
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 1
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 1
            if HDL >= 60:
                risk_score_CVD_sum += -1
            elif 50 <= HDL < 60:
                risk_score_CVD_sum += 0
            elif 40 <= HDL < 50:
                risk_score_CVD_sum += 1
            elif HDL < 40:
                risk_score_CVD_sum += 2
            if is_HT_medicinetreat== False :
                if  SBP < 120 :    
                    risk_score_CVD_sum += 0
                elif 120 <= SBP < 130 :    
                    risk_score_CVD_sum += 0
                elif 130 <= SBP < 140 :    
                    risk_score_CVD_sum += 1
                elif 140 <= SBP < 160 :    
                    risk_score_CVD_sum += 1
                elif SBP >= 160 :    
                    risk_score_CVD_sum += 2
            elif is_HT_medicinetreat== True :
                if  SBP < 120 :    
                    risk_score_CVD_sum += 0
                elif 120 <= SBP < 130 :    
                    risk_score_CVD_sum += 1
                elif 130 <= SBP < 140 :    
                    risk_score_CVD_sum += 2
                elif 140 <= SBP < 160 :    
                    risk_score_CVD_sum += 2
                elif SBP <= 160 :    
                    risk_score_CVD_sum += 3
        elif gender == "female" :
            if 20 <= age < 35 :
                risk_score_CVD_sum += -7
            elif 35 <= age < 40 :
                risk_score_CVD_sum += -3
            elif 40 <= age < 45 :
                risk_score_CVD_sum += 0
            elif 45 <= age < 50 :
                risk_score_CVD_sum += 3
            elif 50 <= age < 55 :
                risk_score_CVD_sum += 6
            elif 55 <= age < 60 :
                risk_score_CVD_sum += 8
            elif 60 <= age < 65 :
                risk_score_CVD_sum += 10
            elif 65 <= age < 70 :
                risk_score_CVD_sum += 12
            elif 70 <= age < 75 :
                risk_score_CVD_sum += 14
            elif 75 <= age < 80 :
                risk_score_CVD_sum += 16
            if TC < 160 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 0
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 0
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 0
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 0
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 0       
            elif 160 <= TC < 200 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 4
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 3
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 2
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 1
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 1
            elif 200 <= TC < 240 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 8
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 6
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 4
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 2
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 1
            elif 240 <= TC < 280 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 11
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 8
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 5
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 3
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 2
            elif  TC >= 280 :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 13
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 10
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 7
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 4
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 2
            elif is_smoke == False :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 0
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 0
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 0
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 0
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 0
            elif is_smoke == True :
                if 20 <= age < 40 :
                    risk_score_CVD_sum += 9
                elif 40 <= age < 50 :
                    risk_score_CVD_sum += 7
                elif 50 <= age < 60 :
                    risk_score_CVD_sum += 4
                elif 60 <= age < 70 :
                    risk_score_CVD_sum += 2
                elif 70 <= age < 80 :
                    risk_score_CVD_sum += 1
            if HDL >= 60 :
                risk_score_CVD_sum += -1
            elif 50 <= HDL < 60:
                risk_score_CVD_sum += 0
            elif 40 <= HDL < 50:
                risk_score_CVD_sum += 1
            elif HDL < 40:
                risk_score_CVD_sum += 2
            if is_HT_medicinetreat== False :
                if  SBP < 120 :    
                    risk_score_CVD_sum += 0
                elif 120 <= SBP < 130 :    
                    risk_score_CVD_sum += 1
                elif 130 <= SBP < 140 :    
                    risk_score_CVD_sum += 2
                elif 140 <= SBP < 160 :    
                    risk_score_CVD_sum += 3
                elif SBP >= 160 :    
                    risk_score_CVD_sum += 4
            elif is_HT_medicinetreat== True :
                if  SBP < 120 :    
                    risk_score_CVD_sum += 0
                elif 120 <= SBP < 130 :    
                    risk_score_CVD_sum += 3
                elif 130 <= SBP < 140 :    
                    risk_score_CVD_sum += 4
                elif 140 <= SBP < 160 :    
                    risk_score_CVD_sum += 5
                elif SBP <= 160 :    
                    risk_score_CVD_sum += 6
        return risk_score_CVD_sum
    else : pass
    
def converter_score_to_percentrisk_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD):
    risk_score_CVD_sum_result =risk_score_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD)
    if gender == "male":
        if risk_score_CVD_sum_result <0:
            risk_score_CVD_sum_result = "<0"
        mappings = {
            "<0": "<1",
            0: 1,
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 4,
            9: 5,
            10: 6,
            11: 8,
            12: 10,
            13: 12,
            14: 16,
            15: 20,
            16: 25,
            17: ">=30"
        }
    elif gender == "female":
        if risk_score_CVD_sum_result <9:
            risk_score_CVD_sum_result = "<9"
        elif risk_score_CVD_sum_result >=25:
            risk_score_CVD_sum_result = ">=25"
        mappings = {
            "<9": "<1",
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 2,
            14: 2,
            15: 3,
            16: 4,
            17: 5,
            18: 6,
            19: 8,
            20: 11,
            21: 14,
            22: 17,
            23: 22,
            24: 27,
            ">=25": ">=30"
        }
    else:
        raise ValueError("Invalid gender")

    if risk_score_CVD_sum_result in mappings:
        return mappings[risk_score_CVD_sum_result]
    else:
        raise ValueError("Invalid SUM Score")




def is_must_lifestylemodification_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD,LDL,FBS,twoHr_postprandial,HbA1c):
    if age >=20 :
        if risk_factor_CVD(is_smoke,SBP,DBP,is_HT_medicinetreat,HDL,family_CHD,gender,age) <=1 and LDL >=160 :
            return "must "
        elif risk_factor_CVD(is_smoke,SBP,DBP,is_HT_medicinetreat,HDL,family_CHD,gender,age) >=2 and risk_score_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD) <=15 and LDL >=130 :
            return "must "
        elif is_CHD == True or is_DM(FBS,twoHr_postprandial,HbA1c) == True or (risk_factor_CVD(is_smoke,SBP,DBP,is_HT_medicinetreat,HDL,family_CHD,gender,age) >=2 and risk_score_CVD(age,gender,is_CHD,TC,is_smoke,HDL,is_HT_medicinetreat,SBP,DBP,family_CHD) >15 and LDL >=100 ):
            return "must "
        else : 
            return "don't need to "
    else : pass

# if age>=18 :
#     print("======BMI======")
#     print("BMI = ",round(BMI_calculation (weight,height),2))
#     print("BMI Class = ",BMI_classification(BMI_calculation (weight,height)))
#     print("Weight management plan = ",is_must_weight_managment(BMI_calculation (weight,height)))
#     print("\n")
#     print("======DM======")
#     print("is DM = ",is_DM())
#     if is_DM() == False: #ไม่เป็นเบาหวาน ความเสี่ยงต้องโชว์ 
#         print("Risk factor DM =" ,risk_factor_DM(BMI_calculation(weight,height)))
#         print("Risk score DM =" ,risk_score_DM(BMI_calculation(weight,height)))
#         if (risk_score_DM(BMI_calculation(weight,height)) is not None) :   #if the 'risk_score_DM' has a value
#             print("ระดับความเสี่ยงต่อโรคเบาหวานใน 12 ปีข้างหน้า ของท่าน ",converter_score_to_percentrisk_DM(risk_score_DM(BMI_calculation(weight,height))))
#     else: pass  #เป็นเบาหวาน ความเสี่ยงต้องไม่โชว์ 
#     print(Lab_fasting_DM())
#     print("DM Lifestyle modification = ",is_must_lifestylemodification_DM())
#     print("\n")
#     print("======HT======")
#     print("HT classification = ",HT_classification(SBP,DBP)[0])
#     print("Risk score HT = ",risk_score_HT())
#     if risk_score_HT() is not None :
#         print(f"Predict 4-year hypertension risk: {converter_score_to_percentrisk_HT(risk_score_HT())[0]}%")
#         print(f"Risk level of HT: {converter_score_to_percentrisk_HT(risk_score_HT())[1]}")
#     else: pass
#     print("HT Lifestyle modification = ",is_must_lifestylemodification_HT())
#     print("\n")
#     print("======CVD======")
#     if age >=20:
#         if is_CHD == False:
#             print("Risk factor CVD = ",risk_factor_CVD())
#             print("Risk score CVD = ",risk_score_CVD())
#             if risk_score_CVD() is not None :
#                 print(f"Predict 10-year CVD risk: {converter_score_to_percentrisk_CVD(risk_score_CVD())}%")
#         print("CVD Lifestyle modification = ",is_must_lifestylemodification_CVD())
#     else: print("CVD Lifestyle modification = ",is_must_lifestylemodification_CVD())
# else: pass


# if age>=18 :
#     st.subheader("======BMI======")
#     st.markdown("BMI = ",round(BMI_calculation (weight,height),2))
#     st.markdown("BMI Class = ",BMI_classification(BMI_calculation (weight,height)))
#     st.markdown("Weight management plan = ",is_must_weight_managment(BMI_calculation (weight,height)))
#     st.markdown("\n")
#     st.subheader("======DM======")
#     st.markdown("is DM = ",is_DM())
#     if is_DM() == False: #ไม่เป็นเบาหวาน ความเสี่ยงต้องโชว์ 
#         st.markdown("Risk factor DM =" ,risk_factor_DM(BMI_calculation(weight,height)))
#         st.markdown("Risk score DM =" ,risk_score_DM(BMI_calculation(weight,height)))
#         if (risk_score_DM(BMI_calculation(weight,height)) is not None) :   #if the 'risk_score_DM' has a value
#             st.markdown("ระดับความเสี่ยงต่อโรคเบาหวานใน 12 ปีข้างหน้า ของท่าน ",converter_score_to_percentrisk_DM(risk_score_DM(BMI_calculation(weight,height))))
#     else: pass  #เป็นเบาหวาน ความเสี่ยงต้องไม่โชว์ 
#     st.markdown(Lab_fasting_DM())
#     st.markdown("DM Lifestyle modification = ",is_must_lifestylemodification_DM())
#     st.markdown("\n")
#     st.subheader("======HT======")
#     st.markdown("HT classification = ",HT_classification(SBP,DBP)[0])
#     st.markdown("Risk score HT = ",risk_score_HT())
#     if risk_score_HT() is not None :
#         st.markdown(f"Predict 4-year hypertension risk: {converter_score_to_percentrisk_HT(risk_score_HT())[0]}%")
#         st.markdown(f"Risk level of HT: {converter_score_to_percentrisk_HT(risk_score_HT())[1]}")
#     else: pass
#     st.markdown("HT Lifestyle modification = ",is_must_lifestylemodification_HT())
#     st.markdown("\n")
#     st.subheader("======CVD======")
#     if age >=20:
#         if is_CHD == False:
#             st.markdown("Risk factor CVD = ",risk_factor_CVD())
#             st.markdown("Risk score CVD = ",risk_score_CVD())
#             if risk_score_CVD() is not None :
#                 st.markdown(f"Predict 10-year CVD risk: {converter_score_to_percentrisk_CVD(risk_score_CVD())}%")
#         st.markdown("CVD Lifestyle modification = ",is_must_lifestylemodification_CVD())
#     else: st.markdown("CVD Lifestyle modification = ",is_must_lifestylemodification_CVD())
# else: pass
