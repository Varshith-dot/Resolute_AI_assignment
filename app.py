import streamlit as st
import pandas as pd

st.title("Machine Learning Tasks Output")

st.header("Task 1: Clustering")
cluster_data = pd.read_csv('output_clusters.csv')
st.write(cluster_data.head())

st.header("Task 2: Classification")
classification_results = pd.read_csv('predictions_rf.csv')
st.write(classification_results.head())

st.header("Task 3: Data Aggregation")
output_data = pd.read_csv('final_output.csv')
st.write(output_data.head())

