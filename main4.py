import streamlit as st

st.title("ELIGIBILITY FOR VOTING")

age = int(st.text_input("Enter your Age    :  ",0))

if age > 18:
    st.success("YOU ARE ELIGIBLE!!!")
if age < 18:
    st.success("YOU ARE NOT ELIGIBLE :( ")
if age == 18:
    st.success("YOU CAN VOTE , ELIGIBLE :)")
