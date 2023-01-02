import streamlit as st

st.title("FINDING AREA WITH SHAPES ")

option = st.selectbox("select the shape to calculate its area",["Square","Rectangle","Circle"])
if option == "Square":
    side = float(st.text_input("Enter Side   :   ",0.0))
    click = st.button("Click here to calculate the Area of Square")
    if click == True:
        Area = side*side
        st.success(Area)

if option == "Rectangle":
    Length = int(st.text_input("Enter Length   :   ",0))
    click2 = st.button("Click here to calculate the Area of Rectangle")
    if click2 == True:
        Area2 = Length*Length
        st.success(Area2)

if option == "Circle":
    radii = float(st.text_input("Enter Radius   :   ",0.0))
    click3 = st.button("Click here to calculate the Area of Circle")
    if click3 == True:
        Area3 = 3.14*radii*radii
        st.success(Area3)


