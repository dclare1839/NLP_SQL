import pandas as pd
import streamlit as st
import description

description_part = description.Description()  # Create an instance of the description_part class

for key, value in st.session_state.dataframes.items():
    description_part.describe_data(key, value)  # Call the method to generate and display the description
    st.divider()
