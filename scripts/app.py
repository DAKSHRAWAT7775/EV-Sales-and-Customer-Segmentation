import streamlit as st
import pandas as pd
import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),"..")))
from data_loading import load_data


# Streamlit page configuration
st.title('EV Sales and Customer Segmentation')

# Sidebar for navigation
st.sidebar.header('User Input')
option = st.sidebar.selectbox('Choose an Action:', ['Load Data', 'Explore Data', 'Train Models'])

# Load Data
if option == 'Load Data':
    df = load_data()
    st.write(df.head())  # Show the first few rows of the dataset
    st.success('Data Loaded Successfully!')

# EDA
elif option == 'Explore Data':
    st.subheader('Exploratory Data Analysis (EDA)')
    st.write("Choose the type of plot:")
    plot_type = st.selectbox('Plot type', ['Sales Analysis', 'Vehicle Classification Analysis'])

    if plot_type == 'Sales Analysis':
        eda_plots.plot_sales(df)
    elif plot_type == 'Vehicle Classification Analysis':
        eda_plots.plot_vehicle_classification(df)

# Train models (Clustering, Regression)
elif option == 'Train Models':
    st.subheader('Model Training')
    clustering_method = st.selectbox('Select Clustering Method:', ['KMeans'])
    if clustering_method == 'KMeans':
        kmeans_model = cluster_data(df)
        st.write("Cluster centers:", kmeans_model.cluster_centers_)
    
    # Sales prediction model
    regression_model = predict_sales(df)
    st.write("Predicted sales: ", regression_model.predict(df.drop(columns=['EV_Sales_Quantity'])))
