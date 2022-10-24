from select import select
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California housing data(1990) by Zhang Jinyi')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
Housing_filter = st.slider('Median House Price:', 0, 500001, 200000)  # min, max, default

# create a multi select
ocean_proximity_filter = st.sidebar.multiselect(
     'Choose  location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a input form
income_filter = st.sidebar.radio('Choose income level',('Low', 'Medium', 'High'))
df = df[df.ocean_proximity.isin(ocean_proximity_filter)]
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income < 4.5) & (df.median_income > 2.5)]
else:
    df = df[df.median_income > 4.5]

# filter by Housing
df = df[df.median_house_value <= Housing_filter]

# filter by capital
df = df[df.ocean_proximity.isin(ocean_proximity_filter)]
# show on map
st.subheader('See more filter in the sidebar')
st.map(df)

# show the plot
st.subheader('Histogram of the Median House Value')

fig, ax = plt.subplots(figsize=(5,5))
median_house_value=df.median_house_value
df.median_house_value.hist(bins=30)



st.pyplot(fig)
