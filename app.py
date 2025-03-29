import streamlit as st
import pandas as pd
import plotly.express as px


vehicles = pd.read_csv('/vehicles_us.csv')


# Histogram Comparing Prices Between Car Models

st.header('Car Models & Prices Comparison')

# List of car models
model_list = sorted(vehicles['model'].unique())

# User input for Car 1
model_1 = st.selectbox(
                    label='Select Model 1',
                    options=model_list,
                    index=model_list.index('ford f-150')
)

# User input for Car 2
model_2 = st.selectbox(
                    label='Select Model 2',
                    options=model_list,
                    index=model_list.index('toyota corolla')
)

# Filtering the dataframe
mask_filter = (vehicles['model'] == model_1) | (vehicles['model'] == model_2)
vehicles_filtered = vehicles[mask_filter]

# Checkbox for user to normalize histogram
normalize = st.checkbox('Normalize Histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# Creating histogram
fig1 = px.histogram(vehicles_filtered,
                    x='price',
                    nbins=100,
                    color='model',
                    histnorm=histnorm,
                    barmode='overlay')

# Displaying with Streamlit
st.write(fig1)




# Scatterplot: Relationship between Price & Model Year

st.header('Price & Model Year Relationship')

fig2 = px.scatter(
    vehicles, 
    x='price', 
    y='odometer',
    width=1200,
    height=800
    )

fig2.update_xaxes(range=[0, 80000])
fig2.update_yaxes(range=[0,500000], dtick=50000)

st.plotly_chart(fig2)
