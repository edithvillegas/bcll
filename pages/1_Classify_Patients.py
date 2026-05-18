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
            Modify the values of the clinical values in the table to obtain the patient prediction.
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
    data=data,
    hide_index=True,
)

# 👉 Add button
if st.button("▶️ Run Prediction"):
    new_data = edited_data.astype("float")
    new_label = predict(new_data.iloc[0])

    st.success(f"Patient belongs to cluster: {new_label}")

    cluster = str(new_label)
    st.image(
                f"data/ALLCASES_cluster_cuminc_cluster_{cluster}.png",
                caption=f"",
                use_container_width=True
            )
    
    #show data about cluster 
    df = pd.read_csv(
    "data/endpoint_bcll.csv",
    sep=";",
    decimal=","
    )

    df = df[df.strata==cluster]["time", "strata", "estimate", "conf.low", "conf.high"]
    df["estimate"]=df["estimate"]*100
    df["conf.low"]=df["conf.low"]*100
    df["conf.high"]=df["estimate"]*100
    
    df.columns = [
        "Time (months)",
        "Cluster",
        "% Patients Treated",
        "Lower Bound (CI)",
        "Higher Bound (CI)"
    ]

    st.dataframe(df)

