import streamlit as st
import requests

st.title("My FastApi Learning Journey")
name=st.text_input("Enter your name here")
if st.button("Say Hello"):
    response=requests.get(f"http://127.0.0.1:8000/hello/{name}")
    st.write(response.json())
    
number2 =st.number_input("Enter a number", step=1)    
if st.button("Calculate Sum"):
    response=requests.get(f"http://127.0.0.1:8000/sum/{number2}")
    st.write(response.json())
    
    
number3 = st.number_input("Enter number", step=1)
if st.button("Multiply"):
    response = requests.get(f"http://127.0.0.1:8000/multiply/{number3}")
    st.write(response.json())
    
seconds = st.slider("Wait seconds", 1, 5)

if st.button("Start Waiting"):
    response = requests.get(f"http://127.0.0.1:8000/delay/{seconds}")
    st.write(response.json())