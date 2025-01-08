import streamlit as st
import pandas as pd 
import numpy as np

import pickle, joblib
from sklearn.cluster import KMeans
import plotly.express as px
import matplotlib.pyplot as plt
import umap

st.set_page_config(
    page_title="BCLL",
    page_icon="data/logo.svg",  # Replace with the path to your image
)
st.logo("data/logo.svg")

st.title("🔬 B-Cell Leukemia Unsupervised Risk Stratification")

# Manually input data
st.subheader("Manually input data")

data = pd.DataFrame({
    "IGHV_%mutation": [0],
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

#load Kmeans
with open("data/kmeans.pickle", 'rb') as file:
    kmeans = pickle.load(file)

#predict new cluster 
stand = pd.read_csv("data/standardization.csv")
new_data = edited_data.astype("float")
new_data = (new_data-stand.T.loc["mean"].values)/stand.T.loc["std"].values
new_label = kmeans.predict(new_data)

st.text(f"Patient belongs to cluster {new_label}")

#UMAP Plot
#load data
umap_embeddings = pd.read_csv("data/umap_embeddings.csv")
umap_embeddings.label = umap_embeddings.label.astype("str")

#plot
label_order = ['1', '2', '3', '4', '5', '6']
colors = [
    "#f0d560", "#5ac8d6", "#98d65a", 
    "#5a83d6", "#e38640", "#c43e37"
]

fig = px.scatter(
    umap_embeddings, 
    x="umap1",
    y="umap2",
    color="label",
    color_discrete_sequence=colors, 
    hover_data={
        "umap1": True, "umap2": True, 
        "label": True,  
    },
    title="UMAP Projection",
    category_orders={"label": label_order},  
)

#add new patient to plot
# with open("data/umap_reducer.pickle", "rb") as file:
#     umap_reducer = pickle.load(file)

#umap_reducer = joblib.load("data/umap_reducer.joblib")

st.text("tuta")

#get umap coordinates
#umap_coordinates = umap_reducer.transform(new_data)
 
# add a single star point for the new patient
fig.add_scatter(
    x=[10],
    y=[10], 
    mode='markers', 
    marker=dict(symbol='star', size=10, color=colors[1]), 
    name='New patient' 
)

#layout 
fig.update_layout(
    xaxis_title="UMAP 1",
    yaxis_title="UMAP 2"
)

fig.update_coloraxes(showscale=False)

st.plotly_chart(fig, theme=None)


