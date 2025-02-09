# Import Streamlit
import streamlit as st

#Header
st.title('🎈 Attrition Prediction')
st.write('Hello world!')

# Importing Toolkits
import pandas as pd
import numpy as np
import plotly.express as px

#import seaborn as sns
import matplotlib.pyplot as plt

#Importing For Modeling
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from xgboost import XGBClassifier
import lightgbm as lgb
from catboost import CatBoostClassifier

# Importing Dash Components
from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc

used_color = ["#ADA2FF", "#C0DEFF", "#FCDDB0", "#FF9F9F", "#EDD2F3", "#98EECC", "#79E0EE"]
# ----------- Loading Dataset -----------
df = pd.read_csv("dataset_final_bytebrains_stage2.csv")
df.head()

# Ubah semua nilai boolean menjadi integer (0 dan 1)
df = df.astype(int)

# Hitung distribusi target Attrition
attrition_counts = df["Attrition"].value_counts()
total = attrition_counts.sum()

# Hitung persentase
attrition_percentages = (attrition_counts / total) * 100

# Visualisasi dengan persentase
plt.figure(figsize=(6,4))
ax = sns.barplot(x=attrition_percentages.index, y=attrition_percentages.values, palette="viridis")

# Menambahkan label persentase di atas setiap bar
for p in ax.patches:
    ax.annotate(f"{p.get_height():.2f}%",
                (p.get_x() + p.get_width() / 2, p.get_height()),
                ha="center", va="bottom", fontsize=12, fontweight="bold")
plt.xlabel("Attrition (0 = Tidak, 1 = Ya)")
plt.ylabel("Persentase (%)")
plt.title("Distribusi Persentase Attrition")
plt.ylim(0, 100)  # Set batas maksimal 100%
plt.show()


