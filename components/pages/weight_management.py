import streamlit as st

def weightcontrol_form():
    physical_activity_list = ['sedentary','lightly active','moderately active','very active','extra active']
    def on_click():
        st.session_state['physical_activity'] = st.session_state.physical_activity_input
        st.session_state['goal_weight'] = st.session_state.goal_weight_input
        st.session_state['current_food_record'] = st.session_state.current_food_record_input
        
    with st.form("weightcontrol_form"):
        st.selectbox('Physical Activity',physical_activity_list,key="physical_activity_input",index=physical_activity_list.index(st.session_state['physical_activity']))
        st.number_input('Goal Weight (kg)',key="goal_weight_input",value=st.session_state['goal_weight'])
        st.number_input('Average Food Record (kcal)',key="current_food_record_input",value=st.session_state['current_food_record'])
        if st.form_submit_button("Submit",on_click=on_click):
            st.session_state['weightcontrol_form_submitted'] += 1