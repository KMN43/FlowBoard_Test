import time
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.read_csv('ExSDReport.csv')

st.set_page_config(
    page_title="Live Dashboard",
    page_icon=":banana:",
    layout="wide"
)

st.title("OB Flow Board")
PPH_filter = st.selectbox("Select Process Path", pd.unique(df['Process Path']))
placeholder = st.empty()


df1 = df[df['Process Path'] == PPH_filter]

PPhs_list = pd.unique(df['Process Path'])

df_total = df.groupby(['Process Path', 'Work Pool']).agg({'Quantity': 'sum'}).reset_index()
PP_SM = df_total.loc[(df_total['Process Path'] == "PPSingleMedium") & (df_total['Work Pool'] == "PickingPicked")]['Quantity']
PP_MM = df_total.loc[(df_total['Process Path'] == "PPMultiMedium") & (df_total['Work Pool'] == "PickingPicked")]['Quantity']
C7 = df_total.loc[df_total['Work Pool'] == "Scanned"]['Quantity']

for seconds in range(200):
    
    with placeholder.container():
        kp1, kp2, kp3 = st.columns(3)
        kp1.metric(label="Picking Picked Single", value= PP_SM+np.random.randint(low=0,high=100))
        kp2.metric(label="Picking Picked Multi", value=PP_MM+np.random.randint(low=0,high=100))
        kp3.metric(label="Scanned", value=C7+np.random.randint(low=0,high=100))
        
    st.markdown("""
    <style>
    div[data-testid="metric-container"] {
   background-color: rgba(28, 131, 225, 0.1);
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 1px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
   
    }

    /* breakline for metric text         */
    div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: white;
   font-size: 20px;
    }
    
    div[data-testid="stMetricValue"] {
    font-size: 100px;
    color: white;
    }
    </style>
    """
    , unsafe_allow_html=True)
    

    
    time.sleep(1)



