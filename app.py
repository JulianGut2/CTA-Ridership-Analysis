import streamlit as st
import pandas as pd

st.set_page_config(page_title = "CTA Ridership",layout = "centered")

st.title("CTA Ridership Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(['Overview', 'EDA',])