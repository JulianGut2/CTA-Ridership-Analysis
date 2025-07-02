import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title = "CTA Ridership", layout = "centered")

st.title("CTA Ridership Dashboard")

# Load in and format our data some
df = pd.read_csv("data/CTA_Ridership_Cleaned.csv")
df['service_date'] = pd.to_datetime(df['service_date'])

# Calculations for further use down the line
df['month_mean'] = df.groupby(['year', 'month'])['total_rides'].transform('mean')
df['month_std'] = df.groupby(['year', 'month'])['total_rides'].transform('std')



# Creating the tabs for our dashboard
tab1, tab2, tab3, tab4 = st.tabs(['Trend', 'Weekday Pattern', 'Extra1', "Extra2"])

with tab1:
    st.subheader("Daily CTA Ridership Over Time")
    fig, ax = plt.subplots(figsize = (14, 5))
    ax.plot(df['service_date'], df['total_rides'], alpha = 0.7)
    ax.set_title("Total Rides Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Total Rides")
    st.pyplot(fig)


with tab2: 
    st.subheader("Average Total Rides by Weekday")
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_avg = df.groupby('weekday')['total_rides'].mean().reindex(weekday_order)
    fig, ax = plt.subplots(figsize = (10, 5))
    sns.barplot(x = weekday_avg.index, y = weekday_avg.values, ax = ax)
    ax.set_title("Average Ridership per Weekday")
    ax.set_ylabel("Average Total Rides")
    st.pyplot(fig)


with tab3:
    st.subheader("Monthly Average Total Rides by Year")
    monthly_avg = df.groupby(['year', 'month'])['total_rides'].mean().unstack(level = 0)
    fig, ax = plt.subplots(figsize = (14, 7))
    sns.heatmap(monthly_avg, annot = True, fmt = ".0f", cmap = "YlGnBu", linewidths = 0.5, ax = ax)
    ax.set_title("Average Monthly CTA Ridership")
    ax.set_ylabel("Month")
    ax.set_xlabel("Year")
    st.pyplot(fig)

with tab4:
    st.subheader("Key Insights & Takeaways")

    top_days = df.sort_values(by = 'total_rides', ascending = False).head(3)