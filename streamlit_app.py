# Import Streamlit
import streamlit as st

#Header
st.title('🎈 Attrition Prediction')
st.write('Hello world!')

# Importing Toolkits
import pandas as pd
import numpy as np
import plotly.express as px

# Importing Dash Components
from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc

used_color = ["#ADA2FF", "#C0DEFF", "#FCDDB0", "#FF9F9F", "#EDD2F3", "#98EECC", "#79E0EE"]
# ----------- Loading Dataset -----------
df = pd.read_csv("dataset_final_bytebrains_stage2.csv")
df.head()

# -------------- Start The Dash App ------------------ #
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

# To render on web app
server = app.server

# Pages Navigator
pages_dict = {
    "Home": "/",
    "Departments": "/Departments",
    "Locations": "/Locations",
    "Performance": "/Performance",
}

# Sidebar Style
sidebar_style = {
    "position": "fixed",
    "width": "16rem",
    "height": "100vh",
    "top": "0",
    "bottom": "0",
    "left": "0",
    "padding": "15px",
    "background-color": "#111",
    "border-right": "2px solid #5FBDFF"
}

# Page Content Style
content_style = {
    "margin-left": "16rem",
    "margin-right": "0rem",
    "padding": "15px",
    "height": "100%",
}

# DropDown Filter Style
filter_style = {
    "border-width": "0px",
    "font-family": "arial",
    "margin-bottom": "25px",
    "background-color": "#222",
}

def get_alert(year_value, department_value):
    return dbc.Alert(
        [
            html.H2("Warning", style={"font": "bold 30px arial"}),
            html.P(
                f"The Department {department_value} Did Not Exist In {year_value} !!😔😔",
                style={"font": "bold 22px arial"}
            ),
            html.Hr(),
            html.P(
                "Choose Another Department",
                style={"font": "bold 20px arial"},
                className="mb-0",
            ),
        ], color="danger",
        style={"box-shadow": "none", "text-shdow": "none"}
    )




