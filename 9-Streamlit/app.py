import streamlit as st
import pandas as pd
import numpy as np

##title of the application
st.title("Hello streamlit")

## Display simple text
st.write("This is a simple text")

##Create a simple dataframe
df =pd.DataFrame({
    'firstcolumn':[1,2,3,4,],
    'secondcolumn':[10,20,30,40]
})

##Display the dataframe
st.write("Here is the datframe")
st.write(df)

##write a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
    )
st.line_chart(chart_data)