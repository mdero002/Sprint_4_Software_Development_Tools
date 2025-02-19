import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt

df = pd.read_csv('vehicles_us.csv')


st.header("""
What factors affect the condition of a vehicle?
""")

st.write("""
### This application helps us to explore what factors can determine the condition a vehicle will be advertized as
""")

# creating checkbox that allows the user to show or hide cars in good conditon within the application
st.write("""
###### Would you like to show or hide cars listed in good condition?
""")
show_good_cars = st.checkbox('Show Good Cars')

if not show_good_cars:
    df = df[df.condition!='good']



# Create a scatter plot to visualize the relationship between the condition of a vehicle and its price use streamlit
st.write('Price vs. Condition')
fig = px.scatter(df, x='price', y='condition', color='condition', labels={'price':'Price'})
st.plotly_chart(fig)




#Create a scatter plot to visualize the relationship between the condition of a vehicle and the odometer reading
st.write('Odometer vs. Condition')
fig = px.scatter(df, x='odometer', y='condition', color='condition', labels={'odometer':'Odometer'})
st.plotly_chart(fig)


# Create a scatter plot to visualize the number of cars listed by condition
st.write('Number of Cars Listed by Condition')
fig = px.scatter(df, x='condition', y='price', color='condition', labels={'condition':'Condition'})
st.plotly_chart(fig)



# Create a histogram to visualize the distribution of days listed basd on the condition of the vehicle
st.write('Distribution of Days Listed by Condition')
fig = px.histogram(df, x='days_listed', color='condition', labels={'days_listed':'Days Listed'})
st.plotly_chart(fig)







