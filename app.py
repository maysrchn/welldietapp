import streamlit as st
from components.state.state import initialize_state
from RiskEngine.RiskEngine import*
initialize_state()
from components.pages.assessment_all import assessment
from components.pages.viewresult import viewresult

#make it look nice from the start
st.set_page_config(layout='wide')

# กดปุ่มแล้วสลับหน้าไปดูผล กดback กลับมาหน้าประเมิน

def viewresult_button():
    def onclick():
        st.session_state.initial_screen =1
        if st.session_state.viewresult_button_input:
            st.session_state.viewresult_button = True
        if st.session_state.viewresult_button:
            st.title('Well Diet')
            st.subheader('NCDs Risk Detection and Lifestyle Modification Therapy heyyyyyy')
            st.caption('by :blue[INVITRACE] เมย์ สรัลชนา')
            viewresult()
            back_button()
    st.button("View Result",on_click=onclick,key="viewresult_button_input")
def back_button():
    def onclick():
        st.session_state.initial_screen =-1
    st.button("Back",on_click=onclick,key="back_button_input")


def main():
    st.title('Well Diet')
    st.subheader('NCDs Risk Detection and Lifestyle Modification Therapy heyyyyyyy')
    st.caption('by :blue[INVITRACE] เมย์ สรัลชนา')
    assessment()  # Display the assessment screen initially
    viewresult_button() # Display the View Result button

if st.session_state.initial_screen <= 0: # Display the assessment screen initially when is (0) or back button (-1)
    main()