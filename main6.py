import streamlit as st

st.title("POSITIVE OR NEGATIVE")

number = int(st.text_input("Enter the Number     :",0))

if number > 0:
    st.success("IT IS A POSITIVE NUMBER !!!!")
if number < 0:
    st.success("IT IS A NEGATIVE NUMBER !!!!")
if number == 0:
    st.success("the number is zero ")

    