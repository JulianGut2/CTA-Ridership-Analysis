import streamlit as st
import pandas as pd

st.set_page_config(page_title = "CTA Ridership",layout = "centered")

st.title("CTA Ridership Dashboard")

df = pd.read.csv("../data/CTA_Ridership_Cleaned.csv")

tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'Data', 'Tab3', 'Tab4])

with tab1:
    st.header("Project Overview")
    st.markdown("---")
    
with tab2:
    st.header("Data")
    st.markdown("---")
   
