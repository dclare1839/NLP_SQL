import pandas as pd
import streamlit as st
import description

if "dataframes" not in st.session_state:
    # To prevent the error when there is no data imported yet.
    st.session_state["dataframes"] = {} 

st.set_page_config(
    page_title="Uploaded File Description", page_icon="📊", layout="wide"
)

if st.session_state.dataframes:
    description_part = description.Description()  # Create an instance of the description_part class

    for key, value in st.session_state.dataframes.items():
        description_part.describe_data(key, value)  # Call the method to generate and display the description
        st.divider()
