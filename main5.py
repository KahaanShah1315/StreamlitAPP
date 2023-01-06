import streamlit as st
title = st.title("CAMERA APP")

picture = st.camera_input("Take a picture")

name = str(st.text_input("Enter Name   : "))
WELCOME = str(st.text_input("YOU ARE A LEGEND ",name))

if picture:
    st.image(picture)
    name = str(st.text_input("Enter Name   : "))