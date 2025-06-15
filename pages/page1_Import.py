import streamlit as st
import pandas as pd
import description  # Import the description module 

# Set up a variable for importing files
st.session_state.uploaded_files = st.file_uploader("Upload CSV files as you wish.", type=["csv"], accept_multiple_files=True)

# Do not work if there is nothing imported yet.
if st.session_state.uploaded_files:
    # If a file is uploaded, read it into a DataFrame
    
    # Set up a variable which is for dataset.
    st.session_state.dataframes = {}

    # Divide the files into separate dataframes
    for file in st.session_state.uploaded_files:
        st.write(f"Successfully imported! - {file.name}")

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)
        data_key = file.name.replace('.csv', '')
        st.session_state.dataframes[data_key] = df