import streamlit as st
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
st.title("MAPS OF INDIA")

Cities = st.text_input("Which City or State do you wanna find")
submit = st.button("Click here to navigate")
geolocator = Nominatim(user_agent="MyApp")

if submit == True:
    location = geolocator.geocode(Cities)

    df = pd.DataFrame(

    [[location.latitude , location.longitude]],
    columns=['lat', 'lon'])

    st.map(df)