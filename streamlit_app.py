import streamlit as st
from rbutton import rbutton_events
from typing import Dict

with st.sidebar:
    st.header("About App")
    st.write("This is my first page")


st.title('🎈 App Name')

st.write('Hello world!')
st.feedback("stars")

input: Dict[str, str] = {
    "name": "Santosh",
    "location": "Pune"
}

value = rbutton_events(input)

if value: 
    st.write("Received", value)
