import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

options = ("GDP", "Happiness", "Generosity")

st.title("In search of happiness")
x = st.selectbox("Select the data for the X-axis", options)
y = st.selectbox("Select the data for the Y-axis", options)

st.subheader(f"{x} and {y}")







