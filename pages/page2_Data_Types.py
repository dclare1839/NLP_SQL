import streamlit as st
import pandas as pd
import set_up_sql

# st.session_state.column_types = {}
def save_settings(dataset_name, key, value):
    # If there is no column_types in session_state, then create a variable.
    if "column_types" not in st.session_state:
        st.session_state.column_types = {}
    # Create a dictionary by dataset
    if dataset_name not in st.session_state.column_types:
        st.session_state.column_types[dataset_name] = {}
    
    # Create a dictionary with key(column name) and value(data type)
    st.session_state.column_types[dataset_name][key] = value
    
    st.write(f"Settings saved for {key}: {value}")


st.set_page_config(
    page_title="Data Types",
    page_icon="📊",
    layout="wide"
)

dtypes = ['String(200)', 'Integer', 'Float', 'Boolean', 'Date', 'Datetime']

if st.session_state.dataframes:
    # for name, dataframe in st.session_state.dataframes.items():
    st.write("Please select the data types for each column in the dataset:")

# Select a dataset from the selectbox
    selected_dataset = st.selectbox(
        "Select Dataset",
        list(st.session_state.dataframes.keys()),
        index=0,
        key="dataset_select"
    )

    dataframe = st.session_state.dataframes[selected_dataset]
    # file_name = selected_dataset

# Select a column from the selectbox
    selected_column = st.selectbox(
        "Select Column",
        dataframe.columns.tolist(),
        index=0,
        key=f"{selected_dataset}_column_select"
    )

# Select a datatype from the selectbox
    selected_type = st.selectbox(
        "Data Types",
        dtypes,
        index=0,
        key=f"{selected_dataset}_{selected_column}_dtype"
    )
    # if st.button("Save Settings", key=f"{selected_dataset}_{selected_column}_save"):
    #     save_settings(selected_dataset, selected_column, selected_type)

    if st.button("Save Settings", key="saving"):
        save_settings(selected_dataset, selected_column, selected_type)

    st.write("Current Data Types for Columns:")
    for name in st.session_state.column_types.keys():
        st.write(st.session_state.column_types[name])

