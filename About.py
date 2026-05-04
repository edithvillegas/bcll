import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="BCLL",
    page_icon="data/logo.svg",  # Replace with the path to your image
)
st.logo("data/logo.svg")

st.title("🔬 B-Cell Leukemia Unsupervised Risk Stratification")

st.markdown("""
This website implements the classifier described in [1] for patient \
            risk stratification in chronic lymphocytic leukemia (CLL), \
            focusing on Time to First Treatment (TTFT). The model is based \
            on the following routinely collected clinical data:

- IGHV gene mutational status, reported as percentage of mutations.
- Trisomy of Chromosome 12 (by FISH), reported as percentage of nuclei with abnormal signal.
- Deletion of Chromosome 11 (by FISH), reported as percentage of nuclei with abnormal signal.
- Deletion of Chromosome 13 (by FISH), reported as percentage of nuclei with abnormal signal.
- CD38 expression detected by flow cytometry, reported as percentage of positive cells.
- CD49d expression detected by flow cytometry, reported as percentage of positive cells.
- Mutational status of TP53, reported as VAF (Variant Allele Fraction).
            
For more information, please refer to the accompanying paper.
""")
st.subheader("References")

st.markdown(
    " \
    1. An Unsupervised Machine Learning Method Stratifies Chronic \
    Lymphocytic Leukemia Patients in Novel Categories with \
    Different Risk of Early Treatment. \
    _Francesca Cuturello, Federico Pozzo, Edith Natalia Villegas Garcia et. Al._ \
    _(Blood, 2022)._  \
    [https://doi.org/10.1182/blood-2022-159981](https://doi.org/10.1182/blood-2022-159981) \
    "
)
