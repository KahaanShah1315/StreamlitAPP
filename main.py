import streamlit as st
st.title("StreamLit Web Apllication")
a = int(st.text_input("Enter the Fist Number!!  : ",0))
b = int(st.text_input("Enter the Second Number!!  : ",0))

c1,c2,c3,c4,c5,c6 = st.columns(6)
with c1:
    button1 = st.button("Click here to ADD")
with c2:
    button2 = st.button("Click here to SUBTRACT")
with c3:
    button3 = st.button("Click here to MULTIPLY")
with c4:
    button4 = st.button("click here to GET EXPONENT")
with c5:
    button5 = st.button("click here to GET MODULE")
with c6:
    button6 = st.button("click here to DIVIDE")

if button1 == True:
    st.success(a+b)

if button2 == True:
    st.success(a-b)

if button3 == True:
    st.success(a*b)

if button4 == True:
    st.success(a**b)

if button5 == True:
    st.success(a%b)

if button6 == True:
    st.success(a/b)


