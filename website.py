import streamlit as st
import pandas as pd
from streamlit import button

st.title("Welcome to Anoop Raj Profile")
st.header("My Profile")
st.subheader("About Me")
st.markdown("I Love My Self")
st.code("""for i in range(1,5,1):
            print("HELLO GUYS")
        """)

dataset = pd.read_csv("Vacancies.xls")

st.dataframe(dataset)

name = st.text_input("Enter Your Name : ")
Fname = st.text_input("Enter Your Father Name : ")
Adress = st.text_area("Enter Your Adress : ")
Qualification = st.selectbox("Enter Your Qualification : ",("Selected","Fresher","Graduated","Post Graduate"))
button = (st.button("Submit"))
if button:
    st.markdown(f"""
    Name: {name}
    Father: {Fname}
    Adress: {Adress}
    Qualification: {Qualification}""")
    
