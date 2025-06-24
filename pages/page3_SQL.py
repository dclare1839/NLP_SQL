import pandas as pd
import streamlit as st
import set_up_sql
import ast
import Gemini_API

def get_prompt():
    prompt = st.text_input("What would you like to know?", key="prompt")
    return prompt;

st.set_page_config(
    page_title="SQL Execution", page_icon="📊", layout="wide"
)
sql = set_up_sql.DatabaseManager()
sql.date_type()
#Create a connection to the database
for name, df in st.session_state.dataframes.items():
    sql.connect('sqlite:///NLP_SQL')
    sql.create_table(name, df)

st.write("Which Result you would like to want?")
st.session_state.prompt_sentence = get_prompt()

gemini = Gemini_API.geminiAPI() #Make an object
gemini.configure() #Configure method

query = gemini.create_sql_query(st.session_state.prompt_sentence, st.session_state.prompt_settings)

sql.execute_query(query)