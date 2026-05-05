import streamlit as st
import pandas as pd 
import numpy as np

import pickle, joblib
from sklearn.cluster import KMeans
import plotly.express as px
import matplotlib.pyplot as plt
import umap

from src.prediction import predict

st.set_page_config(
    page_title="BCLL",
    page_icon="data/logo.svg",  # Replace with the path to your image
)
st.logo("data/logo.svg")

st.title("🔬 B-Cell Leukemia Unsupervised Risk Stratification")

# Manually input data
st.subheader("Manually input data")

st.markdown("""
            Modify the values of the clinical values in the table and the patient 
            prediction will automatically update at the bottom.
            """
            )
            
data = pd.DataFrame({
    "IGHV_mutation": [0],
    "FISH_Tri12": [0],
    "FISH_Del11": [0],
    "CD38": [0],
    "CD49d": [0],
    "TP53": [0],
    "FISH_Del17": [0],
})

edited_data = st.data_editor(
    data = data,
    hide_index=True,
)

#predict new cluster 
new_data = edited_data.astype("float")
new_label = predict(new_data.iloc[0])

st.text(f"Patient belongs to cluster: {new_label}")

