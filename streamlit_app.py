import streamlit as st
import pandas as pd

st.title("🔬 B-Cell Leukemia Unsupervised Risk Stratification")

# Manually input data
st.subheader("Manually input data")

data = pd.DataFrame({
    "Fish_Del17" : [0],
    "%IGHV Mutation": [0],
    "CD49d": [0],
    "CD38": [0],
})

edited_data = st.data_editor(
    data = data,
    hide_index=True,
)

# Batch input
# https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
st.subheader("Batch input")

uploaded_file = st.file_uploader(
    label="Upload a .csv file", 
    type=".csv",
)

st.subheader("References")

st.markdown(
    " \
    An Unsupervised Machine Learning Method Stratifies Chronic \
    Lymphocytic Leukemia Patients in Novel Categories with \
    Different Risk of Early Treatment. \
    _Francesca Cuturello, Federico Pozzo, Edith Natalia Villegas Garcia et. Al._ \
    _(Blood, 2022)._  \
    [https://doi.org/10.1182/blood-2022-159981](https://doi.org/10.1182/blood-2022-159981) \
    "
)