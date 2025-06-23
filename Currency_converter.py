import streamlit as st
import requests

st.title("Live Currency Converter")
amnt = st.number_input("Enter Amount in INR", min_value = 1)

targett_currency = st.selectbox("Convert to:", ["USD","EUR","JPY","GBP"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        rate = data["rates"][targett_currency]
        converted = rate*amnt
        st.success(f'{amnt} INR = {converted: .2f} {targett_currency}')