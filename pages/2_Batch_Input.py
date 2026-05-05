import streamlit as st
import pandas as pd
from src.prediction import predict

st.set_page_config(
    page_title="BCLL",
    page_icon="data/logo.svg",  # Replace with the path to your image
)
st.logo("data/logo.svg")

st.title("🔬 B-Cell Leukemia Unsupervised Risk Stratification")

st.markdown("""
            Here you can upload your patient data as a CSV file to make batch predictions.
            Each row is a patient and each column is a clinical varible.
            For an example of how the data should be formatted take a look at this test data:
            [Example CSV file](https://raw.githubusercontent.com/edithvillegas/bcll/refs/heads/main/data/test_dataset.csv)
            """
            )


# Batch input
# https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
st.subheader("Batch input")

uploaded_file = st.file_uploader(
    label="Upload a .csv file", 
    type=".csv",
)

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, sep=",")
    st.dataframe(dataframe, hide_index=True)
    dataframe["prediction"] = dataframe.apply(predict, axis=1)

    st.subheader("📊 Prediction Results")
    st.dataframe(dataframe, hide_index=True)

    st.subheader("⬇️ Download Results")

    csv = dataframe.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download predictions as CSV",
        data=csv,
        file_name="predictions.csv",
        mime="text/csv",
    )

    