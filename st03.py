import time
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.read_csv('ExSDReport.csv')

st.set_page_config(
    page_title="Live Dashboard",
    layout="wide"
)

st.title("OB Flow Board")
PPH_filter = st.selectbox("Select Process Path", pd.unique(df['Process Path']))
placeholder = st.empty()


df1 = df[df['Process Path'] == PPH_filter]

PPhs_list = pd.unique(df['Process Path'])

df_total = df.groupby(['Process Path', 'Work Pool']).agg({'Quantity': 'sum'}).reset_index()
pip
PP_SM= df_total.loc[(df_total['Process Path'] == "PPSingleMedium") & (df_total['Work Pool'] == "PickingPicked")]['Quantity']
PP_MM= df_total.loc[(df_total['Process Path'] == "PPMultiMedium") & (df_total['Work Pool'] == "PickingPicked")]['Quantity']

for seconds in range(200):
    
    with placeholder.container():
        kp1, kp2, kp3 = st.columns(3)
        kp1.metric(label="Picking Picked Single", value= PP_SM+np.random.randint(low=0,high=100))
        kp2.metric(label="Picking Picked Multi", value=PP_MM+np.random.randint(low=0,high=100))


    
    time.sleep(1)



