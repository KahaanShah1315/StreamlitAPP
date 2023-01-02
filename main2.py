import streamlit as st

st.title("Body Mass Index")

H = float(st.text_input("ENTER YOUR HEIGHT    :"))

W = int(st.text_input("ENTER YOUR WEIGHT    :"))

BODY_MASS = st.button("Click here to fine BODY MASS INDEX")


if BODY_MASS == True:
    BMI = W/(H*H)
    st.success(BMI)

    if BMI < 16:

        st.success("YOU ARE UNDER NOURISHED!!!!")

    elif BMI < 26:

        st.success("YOU ARE HEALTH AND FINE!!!!")

    elif BMI > 26:

        st.success("YOU HAVE OBESITY!!!!")

