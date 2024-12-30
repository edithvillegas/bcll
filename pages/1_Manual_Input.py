import streamlit as st
import pandas as pd

st.title("🔬 B-Cell Leukemia Unsupervised Risk Stratification")

# Manually input data
st.subheader("Manually input data")

data = pd.DataFrame({
    "CD49d": [0],
    "CD38": [0],
    "Fish_Del17": [0],
    "Fish_Del11": [0],
    "Fish_Tri12": [0],
    "%IGHV_Mutation": [0],
})

edited_data = st.data_editor(
    data = data,
    hide_index=True,
)

st.text(f"Patient belongs to cluster {edited_data.CD49d[0]}")