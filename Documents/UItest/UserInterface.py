#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 13:28:13 2021

@author: mtdsoe
"""
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image




selection_name =pd.DataFrame({'col1': ["Male","Female","Gay"]})



with st.form("my_form"):

    st.caption('Fill In the blank')
    st.text_input("First Name",key="fname")
    st.text_input("Middle Name",key="mname")
    st.text_input("Last Name",key="lname")
    st.text_input("Email",key="email")
    st.text_input("Contact Address",key="caddress")
    st.text_input("Permanent Address",key="paddress")
    add_selectbox = st.sidebar.selectbox(
    "How would you like to do?",
    ("Creat User", "Update User", "Delete User"))


   
    st.selectbox("Choose",selection_name)
    header_html = "<img src='./UItest/logo.png' class='img-fluid'>"
    st.markdown(
    header_html, unsafe_allow_html=True,
    )
    checkbox_val = st.checkbox("Agree my terms")
    slider_val = st.slider("Form slider")
    chart_data = pd.DataFrame(np.random.randn(20,3),
                              columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

