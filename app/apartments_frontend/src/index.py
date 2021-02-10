import streamlit as st
import requests
url = 'http://backend-service:5000/api/apartments'
response = requests.get(url)
apartments = response.json()

st.write("""
# My first app
Hello *world!*
""")


st.write(apartments)

