import streamlit as st
import plotly.express as px
import pandas as pd

options = ("GDP", "Happiness", "Generosity")

# Add title widget
st.title("In search of happiness")

# Add two selectboxes
option_x = st.selectbox("Select the data for the X-axis", options)
option_y = st.selectbox("Select the data for the Y-axis", options)

# Load the dataframe
df = pd.read_csv("happy.csv")

# Match value for X-axis
match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

# Match value for Y-axis
match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

# Add subheader for the plot
st.subheader(f"{option_x} and {option_y}")

# Create the plot and add to the page
figure = px.scatter(x=x_array, y=y_array, labels={"x":option_x, "y":option_y})
st.plotly_chart(figure)




