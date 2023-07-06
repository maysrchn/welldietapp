#stage page listen whan change ==change

import streamlit as st
from streamlit_option_menu import option_menu

def streamlit_menu():
    # 2. horizontal menu w/o custom style
    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "Projects", "Contact"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected