import streamlit as st
import pandas as pd 
import numpy as np

import pickle, joblib
from sklearn.cluster import KMeans
import plotly.express as px
import matplotlib.pyplot as plt
import umap

from src.prediction import predict, predict_bool

st.set_page_config(
    page_title="BCLL",
    page_icon="data/logo.svg",  # Replace with the path to your image
)
st.logo("data/logo.svg")

st.title("🔬 B-Cell Leukemia Unsupervised Risk Stratification")

st.markdown("""
            Modify the values of the clinical variables to obtain the patient prediction. 
            You can choose to either input the numeric values or reply to a series of yes/no questions.
            """
            )
            
input_questions = st.toggle("Toggle to change between numeric values or answer yes/no questions.")

if input_questions:
    st.subheader("Answer Yes/No questions")

    #input variables
    patient = dict()
    patient["TP53_above"] = st.toggle("Is the value of TP53 above 36 ?")
    patient["FISH_Del11_above"] = st.toggle("Is the value of FISH_Del11 above 34 ?")
    patient["FISH_Tri12_above"] = st.toggle("Is the value of FISH_Tri12 above 20 ?")
    patient["IGHV_mutation_above"] = st.toggle("Is the value of IGHV_mutation above 9 ?")
    patient["CD49d_above"] = st.toggle("Is the value of CD49d above 42 ?")
    patient["CD38_above"] = st.toggle("Is the value of CD38 above 42 ?")
    patient["IGHV_mutation_above2"] = st.toggle("Is the value of IGHV_mutation above 3 ?")

else:
    st.subheader("Input Numeric Values")

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
    if input_questions:
        new_label = predict_bool(patient)
    else:
        new_label = predict(edited_data.astype("float").iloc[0])
    
    st.success(f"Patient belongs to cluster: {new_label}")

    #cluster data
    cluster = int(new_label)

    #cluster description
    match cluster:
        case 1:
            st.markdown("""
                    Clusters 1 gathers CLL cases which are negative for all features (CD38, CD49d, chromosomal aberrations, TP53 mutations) but have unmutated or borderline-mutated (97-100% of germline identity) IGHV genes. The prognosis is intermediate, with no significant stratification between true IGHV-unmutated cases and borderline-mutated cases.
                    """)
        case 2:
            st.markdown(
                """
                Cluster 2 gathers CLL cases which are negative for all features (CD38, CD49d, chromosomal aberrations, TP53 mutations) but have mutated IGHV genes (91-97% of germline identity) IGHV genes. Cluster 2 associates with long telomeres and overall genetic stability. The prognosis is favorable.
                """
            )
        case 3:
            st.markdown("""
                Cluster 3 gathers CLL cases which are negative for all features (CD38, CD49d, chromosomal aberrations, TP53 mutations) and have highly- mutated IGHV genes (less than 91% of germline identity). Cluster 3, similarly to cluster 2,  associates with long telomeres and overall genetic stability. The prognosis is favorable.            
                        """)
        case 4:
            st.markdown("""
                Cluster 4 includes patients showing expression of the CD49d integrin and/or CD38. These cases do not carry significant chromosomal aberrations or TP53 mutations. Immunoglobulin genes can be either mutated or unmutated.  The prognosis is intermediate.            
                        """)
        case 5:
            st.markdown("""
                Cluster 5 is constituted by patients with trisomy 12; this chromosomal aberration strongly associated with expression of CD49d and CD38. Immunoglobulin genes can be variably mutated, but carry limited prognostic significance. The prognosis is intermediate-low.
                        """)
        case 6:
            st.markdown("""
                Cluster 6 gathers patients with elevated del(11q) levels; IGHV genes are mostly unmutated; TP53 disruption (mutation or deletion) is generally mutually exclusive. Telomeres are significantly shorter than other clusters and suggest a degree of chromosomal instability. The prognosis is mostly unfavorable.
                        """)
        case 7:
            st.markdown("""
                Cluster 7 includes patients with TP53 disruption with high mutation burden and/or del(17p). Other features such as trisomy 12, del(11q) and CD38 are frequently negative; CD49d can be variably expressed, as well as IGHV mutation, but these features do not add significant prognostic information. This cluster associates with short telomere length, suggesting presence of chromosomal instability. The prognosis is unfavorable.
                        """)

    
    cluster = str(new_label)
    #show data about cluster 
    df = pd.read_csv(
    "data/endpoint_bcll.csv",
    sep=";",
    decimal=","
    )

    df.strata = df.strata.astype('str')
    df = df[df.strata==cluster][["time", "estimate", "conf.low", "conf.high"]]
    df["estimate"]=df["estimate"]*100
    df["conf.low"]=df["conf.low"]*100
    df["conf.high"]=df["conf.high"]*100
    
    df.columns = [
        "Time (months)",
        "% Risk of Treatment",
        "Lower Bound (CI)",
        "Higher Bound (CI)"
    ]

    column_config = {
        col: st.column_config.NumberColumn(format="%.1f")
        for col in df.select_dtypes("float").columns
    }

    st.dataframe(
        df,
        hide_index=True,
        column_config=column_config
    )

    st.image(
                f"data/ALLCASES_cluster_cuminc_cluster_{cluster}.png",
                caption=f"",
                use_container_width=True
            )

