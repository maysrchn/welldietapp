#stage page listen whan change ==change

# import streamlit as st
# from streamlit_option_menu import option_menu

# def streamlit_menu():
#     # 2. horizontal menu w/o custom style
#     selected = option_menu(
#         menu_title=None,  # required
#         options=["BMI", "Weight Control", "Hypertension", "Cardiovascular", "Diabetes"],  # required
#         # icons=["house", "book", "envelope"],  # optional
#         # menu_icon="cast",  # optional
#         default_index=0,  # optional
#         orientation="horizontal",
#     )
#     return selected

import streamlit as st
import hydralit_components as hc

# # specify the primary menu definition
# def streamlit_menu():
#         menu_data = [
#                 {'icon': "far fa-copy", 'label':"Left End"},
#                 {'id':'Copy','icon':"🐙",'label':"Copy"},
#                 {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
#                 {'icon': "far fa-address-book", 'label':"Book"},
#                 {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
#                 {'icon': "far fa-clone", 'label':"Component"},
#                 {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
#                 {'icon': "far fa-copy", 'label':"Right End"},
#         ]
#         # we can override any part of the primary colors of the menu
#         #over_theme = {'txc_inactive': '#FFFFFF','menu_background':'red','txc_active':'yellow','option_active':'blue'}
#         over_theme = {'txc_inactive': '#FFFFFF'}
#         menu_id = hc.nav_bar(menu_definition=menu_data,home_name='Home',override_theme=over_theme)


#         #get the id of the menu item clicked
#         st.info(f"{menu_id=}")
#         return menu_data



def streamlit_menu():
        # specify the primary menu definition
        menu_data = [
        {'id':'Profile','icon': "bi bi-person-fill", 'label':"Profile"},
        {'id':'BMI','icon':"bi bi-caret-right-fill",'label':"BMI"},
        {'id':'Weight Control','icon': "bi bi-caret-right-fill",'label':"Weight Control"},
        {'id':'Hypertension','icon': "bi bi-caret-right-fill", 'label':"Hypertension"},#no tooltip message
        {'id':'Cardiovascular','icon': "bi bi-caret-right-fill", 'label':"Cardiovascular"},
        {'id':'Diabetes','icon': "bi bi-caret-right-fill", 'label':"Diabetes"}, #can add a tooltip message ''','ttip':"I'm the Dashboard tooltip!"'''
        ]

        over_theme = {'txc_inactive': '#FFFFFF'}
        menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        # home_name='Home',
        # login_name='Logout',
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=True, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
        )

        # if st.sidebar.button('click me too'):
        #         st.info('You clicked at: {}'.format(datetime.datetime.now()))

        #get the id of the menu item clicked
        
        return menu_id