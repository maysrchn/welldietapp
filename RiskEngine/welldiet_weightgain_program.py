# โปรแกรมเพิ่มน้ำหนัก
# เมื่อคุณต้องเพิ่มน้ำหนัก จากการประเมิน ให้ทำการ set น้ำหนักเป้าหมายที่สูงกว่าน้ำหนักปัจจุบัน
# ดูว่าตอนนี้กิน current_food_record เท่าไหร่ แล้วควรเพิ่มให้ถึงกี่กิโลที่อยู่ในเกณฑ์สมส่วน
# ค่อยๆ step จากที่กิน ตามบันไดการ step up 
# จนกระทั่งถึงจุดที่จะเพิ่มน้ำหนักได้เร็ว 0.5 kg/week 
import streamlit as st
# import matplotlib.pyplot as plt
import datetime

def weight_gain_module(age, gender, height, current_weight, physical_activity, goal_weight,current_food_record):
    def weight_loss_program(age, gender, height, current_weight, physical_activity, goal_weight):
        # Calculate BMR using the Mifflin-St Jeor equation
        if gender == 'male':
            bmr = 10 * current_weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * current_weight + 6.25 * height - 5 * age - 161
        
        # Calculate TDEE based on physical activity level
        activity_factors = {
            'sedentary': 1.2,
            'lightly active': 1.375,
            'moderately active': 1.55,
            'very active': 1.725,
            'extra active': 1.9
        }
        
        if physical_activity not in activity_factors:
            print("Invalid physical activity level.")
            return
        
        tdee = bmr * activity_factors[physical_activity]
        error0=None
        # Check if the goal weight is within the BMI range of 18.5 - 22.9
        goal_bmi = goal_weight / ((height / 100) ** 2)
        if goal_bmi < 18.5 or goal_bmi > 22.9:
            error0="Note : Goal weight is not within the BMI range of 18.5 - 22.9."

        
        # Calculate goal date
        weight_loss_rate = 0.5  # Initial weight loss rate per week
        # if tdee-current_food_record > ((7700/7)*0.5):
        #     weight_loss_rate = (7700/2)/((tdee-current_food_record)*7)

        total_weight_loss = goal_weight - current_weight
        weeks_to_lose_weight = total_weight_loss / weight_loss_rate
        goal_date = datetime.datetime.now() + datetime.timedelta(weeks=weeks_to_lose_weight)
        
        # Calculate length of time
        time_delta = goal_date - datetime.datetime.now()
        years = time_delta.days // 365
        months = (time_delta.days % 365) // 30
        days = (time_delta.days % 365) % 30
        
        # Calculate daily calorie budget
        goal_calorie_budget = tdee + (weight_loss_rate * 7700 / 7)
        
        error1=None
        # Adjust weight loss rate if daily calorie budget is below BMR
        while goal_calorie_budget < bmr: #######################
            weight_loss_rate -= 0.02
            weeks_to_lose_weight = total_weight_loss / weight_loss_rate
            goal_date = datetime.datetime.now() + datetime.timedelta(weeks=weeks_to_lose_weight)
            time_delta = goal_date - datetime.datetime.now()
            years = time_delta.days // 365
            months = (time_delta.days % 365) // 30
            days = (time_delta.days % 365) % 30
            goal_calorie_budget = tdee - (weight_loss_rate * 7700 / 7)
            if weight_loss_rate <= 0:
                error1 ="Unable to achieve the goal weight within the specified BMI range."
                return None
        
        # Print output
        # st.markdown("======== weight loss profile ===========")
        # st.markdown(f"TDEE: {round(tdee)} kcal")
        # st.markdown(f"BMR: {round(bmr)} kcal")
        # st.markdown(f"Goal date: {goal_date.strftime('%Y-%m-%d')}")
        # st.markdown(f"Length of time: {years} years, {months} months, {days} days")
        # st.markdown(f"Number of weeks : {weeks_to_lose_weight}")
        # st.markdown(f"Goal calorie budget: {round(goal_calorie_budget)} kcal")
        # st.markdown(f"Total weight gain: {total_weight_loss} kg")
        # st.markdown(f"Weight gain rate per week: {round(weight_loss_rate,2)} kg/week")
        return tdee,goal_calorie_budget,activity_factors,weight_loss_rate,bmr,total_weight_loss,error0,error1


    # Example usage
    list_result=weight_loss_program(age, gender, height, current_weight, physical_activity, goal_weight)
    if list_result is None : 
        return None
    tdee = list_result[0]
    bmr = list_result[4]
    activity_factors=list_result[2]
    weight_loss_rate = list_result[3]
    total_weight_loss = list_result[5]
    error0=list_result[6]
    error1=list_result[7]
    #=================
    goal_calorie_budget = list_result[1]

    eat_over_or_under_factor = current_food_record / tdee

    calories_factor_goal = [1.750 ,1.625 ,1.5, 1.375, 1.25, 1.125, 1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]



    # Find the index of the calories factor goal that eat_over_or_under_factor falls between
    error2=None
    daily_calories_budget = []
    for i in range(len(calories_factor_goal) - 1, -1, -1):
        budget = current_food_record * calories_factor_goal[i]
        daily_calories_budget.append(budget)
        last_week_budget = daily_calories_budget[-1]
        if last_week_budget > goal_calorie_budget:
            break
    if current_food_record < bmr:
            error2="current food record is below than BMR"
    else:
        index = daily_calories_budget.index(current_food_record)
        daily_calories_budget = daily_calories_budget[index:]




    if  current_food_record < bmr:
        return None

    weekly_goal_list=[]
    # Adjust the last week's budget to match the goal calorie budget
    last_week_budget = daily_calories_budget[-1]
    if last_week_budget > goal_calorie_budget:
        daily_calories_budget[-1] = goal_calorie_budget
    # if current_food_record < goal_calorie_budget:
    #     goal_calorie_budget =weight_loss_rate
    # st.markdown("\n")
    # st.markdown("=============== For Well Diet Invitrace App ==============")
    # st.markdown("=== A.I. Stepping Calories goal increase Week by Week ====")
    # Print the daily calorie budget for each week
    for i, budget in enumerate(daily_calories_budget):
        if i > 0:  # Skip printing for Week 0
            weekly_goal=(f"Week {i}: {round(budget)} kcal")
            weekly_goal_list.append(weekly_goal)
    # สำหรับพยากรณ์น้ำหนักจากที่กิน

    # Create lists to store weight and week number

    weightgain_list = [current_weight]
    day_list_weightgain = [0]
    current_food_record_list = []

    def loopweightgain (current_food_record,current_weight,i):
        if gender == 'male':
            tdee_realtime = ((10 * current_weight) + (6.25 * height) - (5 * (age +(i*(1/365)))) + 5) *activity_factors[physical_activity]
        else:
            tdee_realtime = ((10 * current_weight) + (6.25 * height) - (5 * (age +(i*(1/365)))) - 161)*activity_factors[physical_activity]
        weight_gain = (current_food_record - tdee_realtime) / 7700
        current_weight += weight_gain
        weightgain_list.append(current_weight)
        day_list_weightgain.append(i)
        current_food_record_list.append(current_food_record)
        return weightgain_list,day_list_weightgain

    weightloss_list = [current_weight]
    day_list_weightloss = [0]
    # =========
    daily_calories_budget_each_day = []
    if weight_loss_rate >= 0.5:
        for budget in daily_calories_budget:
            daily_calories_budget_each_day.extend([budget] * 7)
    else:
        for budget in daily_calories_budget:
            daily_calories_budget_each_day.extend([budget] * 7)
        if len(daily_calories_budget_each_day) > 7:
            daily_calories_budget_each_day = daily_calories_budget_each_day[7:]

    x=0
    # =========
    def loopweightloss (daily_calories_budget_each_day,current_weight,x):
        if gender == 'male':
            tdee_realtime = ((10 * current_weight) + (6.25 * height) - (5 * (age +(x*(1/365)))) + 5) *activity_factors[physical_activity]
        else:
            tdee_realtime = ((10 * current_weight) + (6.25 * height) - (5 * (age +(x*(1/365)))) - 161)*activity_factors[physical_activity]
        weight_stepdown = (daily_calories_budget_each_day[x] - tdee_realtime) / 7700
        current_weight += weight_stepdown
        weightloss_list.append(current_weight)
        day_list_weightloss.append(x)
        current_food_record_list.append(current_food_record)
        return weightloss_list

    while weightloss_list[-1]<goal_weight:
        # print(x)
        # print(weightloss_list[-1])
        # print(daily_calories_budget_each_day[x])
        x += 1
        daily_calories_budget_each_day.append(daily_calories_budget_each_day[-1])
        loopweightloss (daily_calories_budget_each_day,weightloss_list[-1],x)
        if x >1000: #### เปลี่ยนวันสูงสุดที่จะโชว์ได้ ระวังเยอะเกินจนเครื่อง crash
            break
        if weightloss_list[-1]>=goal_weight:
            break
        if weightloss_list[-1]<weightloss_list[0]*0.80:
            break

    # for i in range (1,365) :
    #     loopweightgain (current_food_record,weightgain_list[-1],i)
    from datetime import date
    from dateutil.relativedelta import relativedelta

    def convert_days_to_length_of_time(days):
        today = date.today()
        target_date = today + relativedelta(days=days)
        length_of_time = relativedelta(target_date, today)
        
        years = length_of_time.years
        months = length_of_time.months
        days = length_of_time.days
        
        return years, months, days

    # # Example usage
    # st.markdown("\n")
    # st.markdown(f"number of days : {day_list_weightloss[-1]} days")
    days = day_list_weightloss[-1]
    years, months, days = convert_days_to_length_of_time(days)
    # st.markdown(f"Length of time Actually: {years} years, {months} months, {days} days")
    return round(tdee),round(bmr),"For weight gain",(f"Goal calorie budget: \n {round(goal_calorie_budget)} kcal"),(f"Total weight loss: \n {total_weight_loss} kg"),(f"Weight loss rate per week: \n {round(weight_loss_rate,2)} kg/week"),weekly_goal_list,(f"number of days \n {day_list_weightloss[-1]} days"),(f"Length of time Actually  \n {years} years, {months} months, {days} days"),error0,error1,error2
    # plt.plot(day_list_weightloss, weightloss_list)
    # plt.xlabel('day')
    # plt.ylabel('Weight (kg)')
    # plt.title('Weight Loss over Time')
    # plt.show()


