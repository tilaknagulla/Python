import streamlit as st
import pandas as pd
st.title("This is my app")
name=st.text_input("Enter your name")
if name:
    st.write(f"hello {name}")
age=st.slider("Select your age",0,100,25)
st.write(f"Your age is {age}")

options=['C','JAVA','PYTHON','JAVA SCRIPT']
choice=st.selectbox("Choose your favorite language",options)
st.write(f"selected choice {choice}")


data={
    "name":["Tilak","Syamala","Srinivasa Rao","Krishna Kumari"],
    "city":["Dubai","Hyderabad","Elamarru","Elamarru"],
    "age":[27,29,57,47]
}
df =pd.DataFrame(data)
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)
