# Sprint_4_Software_Development_Tools

# Introduction
In this project, I was asked to develop and deploy a web application to a cloud service so that it would be accessible to the public. The application is based on a dataset of vehicle sales advertisements.

# Exploratory Data Analysis
Using a Jupyter Notebook, I imported the following libraries to explore the dataset: pandas, numpy, matplotlib, streamlit, plotly, altair, and seaborn.

I reviewed the data to see what information was provided:
The initial exploration of the data shows the following:
There are 51525 entries in this data set
There are 13 columns in this data set that are as follows:
    Price- price of the vehicle
    model_year - year of the vehicles
    model- model of the vehicle
    condition- condition of the vehicle
    cylinders- number of engine cylinders
    fuel - type of fuel
    odometer- mileage on the vehicle at the time of the ad
    transmission- type of transmission
    paint_color- color of the vehicle
    is-4wd- if the vehicle has 4 wheel drive
    date_posted- the date the ad was posted
    days_listed- the number of days the ad ran 

I cleaned the data by checking for duplicates, filling in missing values, and changing data types as needed. 

 I used the median approach based on the model of the Vehicles  to replace     
 missing values for the model year and cylinders.

 I used the median approach based on the condition of the vehicle to replace 
  missing values for the odometer reading.

I also created columns several new columns for further data analysis.

I focused my data approach on exploring if certain factors about a vehicle could be used to predict the condition in which it would be advertised.

I also explored to see if the condition impacted the number of days the vehicle ad remained active.

# Web Application Dashboard
Using an app.py file in the root directory, I created a web application using render. I used plotly and streamlit for data visualization

The web application allows viewers to:

  See scatterplots representing the two factors that were the most significant predictors in determining the condition of a   vehicle (price and odometer reading). 

   See a histogram of the average day vehicles in each condition were advertised on the site. 

  See a bar graph showing the number of vehicles listed in each condition.


Additionally, Viewers can interact with the web application by selecting to see vehicles listed in good condition (which was the most challenging condition to predict using the selected factors).

# Project Deployment
The application has been configured for deployment on Render. To do this, I created a requirements.txt in the root level of the project's folder. I added the following packages:
    pandas===2.0.3
    scipy==1.11.1
    streamlit--1.25.0
    altair==5.0.1
    plotly==5.15.0

I then created a .streamlit directory then added a config.toml file. I added the following content to the file: 
    [server]
    headless = true
    port = 1000

    [browser]
    serverAddress = "0.0.0.0"
    serverPort = 1000

The configuration file was used to tell Render where to look in order to listen to my Streamlit app when hosting it on its servers. 

After creating my account on Render, I created a new web service. I connected this web service to my project's GitHub repository. I configured the Render web service using the command pip install streamlit & install -r requirements.txt.

I used the start command streamlit run app.py

I deployed the project to Render and checked that the installation was successful and that the application was accessible using its web address. 

# Website Link
https://sprint-4-software-development-tools-x4m8.onrender.com



