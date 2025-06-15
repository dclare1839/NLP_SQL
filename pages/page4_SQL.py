import pandas as pd
import streamlit as st
import google.generativeai as genai
import os
import set_up_sql
import Gemini_API
import ast


#Create a connection to the database
sql = set_up_sql.DatabaseManager()
sql.connect('sqlite:///cyber_security.db')
sql.create_table(df)


# def extract_select_statements(text):
#     """
#     Extracts SQL SELECT statements from a given text using regex.
#     """
#     # 기본 패턴: SELECT로 시작해서 ;로 끝나는 문장
#     pattern = r'SELECT.*?;'

# description_part = description.Description_part()

# if st.session_state.uploaded_files:
#     # If a file is uploaded, read it into a DataFrame
    
#     dataframes = {}

#     for uploaded_file in st.session_state.uploaded_files:
#         # Read the CSV file into a DataFrame
#         df = pd.read_csv(uploaded_file)
#         data_key = uploaded_file.name.replace('.csv', '')
#         dataframes[data_key] = df

#     for key, value in dataframes.items():
#         description_part.describe_data(key, value)  # Call the method to generate and display the description
