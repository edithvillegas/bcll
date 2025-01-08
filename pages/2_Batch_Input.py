import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="BCLL",
    page_icon="data/logo.svg",  # Replace with the path to your image
)
st.logo("data/logo.svg")

st.title("🔬 B-Cell Leukemia Unsupervised Risk Stratification")

# Batch input
# https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
st.subheader("Batch input")

uploaded_file = st.file_uploader(
    label="Upload a .csv file", 
    type=".csv",
)

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.dataframe(dataframe, hide_index=True)

    st.text(f"Patient belongs to cluster {dataframe.CD49d[0]}")