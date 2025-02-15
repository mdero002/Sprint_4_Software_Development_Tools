import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import altair as alt

df = pd.read_csv('../vehicles_us.csv')

# Fill in missing values with the string 'unknown'
df['paint_color'] = df['paint_color'].fillna('unknown')

# Recheck the value counts for the paint_color column
df['paint_color'].value_counts(dropna=False)

# Check for missing values in the model_year column
df['model_year'].value_counts(dropna=False)

# Replace missing values in the model_year column with the median values for each model
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.median()))

# Recheck the missing values in the model_year column
df['model_year'].value_counts(dropna=False)

# Replace missing values in the cylinders column with the median values for each model
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))

# Recheck the missing values in the cylinders column
df['cylinders'].value_counts(dropna=False)

# Replace missing values in the odometer column with the median values for each condition
df['odometer'] = df.groupby('condition')['odometer'].transform(lambda x: x.fillna(x.median()))

# Recheck the missing values in the odometer column
df['odometer'].value_counts(dropna=False)

# Change model_year, cylinders, and odometer columns to integer data type
df['model_year'] = df['model_year'].astype('int')  

df['cylinders'] = df['cylinders'].astype('int')  

df['odometer'] = df['odometer'].astype('int')  

# Change is_4wd column to boolean data type
df['is_4wd'] = df['is_4wd'].astype(bool)

# Change date_posted column to datetime data type
df['date_posted'] = pd.to_datetime(df['date_posted'], format='%Y-%m-%d')

# Add a new column that calculates the vehicle's age when the ad was placed
df['vehicle_age'] = df['date_posted'].dt.year - df['model_year']

# Add a new column that calculates the vehicle's average mileage per year rounded to the nearest whole number   
df['average_mileage'] = df['odometer'] / df['vehicle_age']
df['average_mileage'] = df['average_mileage'].round(0)

# Replace values of 0 in the vehicle_age column with 1
df['vehicle_age'] = df['vehicle_age'].replace(0, 1)

# Replave missing values in the average_mileage column with 0
df['average_mileage'] = df['average_mileage'].fillna(0)

# Create a new column for the make of the vehicle
df['make'] = df['model'].str.split(' ', expand=True)[0]

# Streamlit code for bar graph of average price by paint color
st.write('Average Price by Paint Color')
fig = px.bar(pivot_table, x=pivot_table.index, y='price', color='price', labels={'price':'Average Price'})  
st.plotly_chart(fig)

