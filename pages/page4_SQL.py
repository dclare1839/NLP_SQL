import pandas as pd
import streamlit as st
import set_up_sql
import ast

def get_prompt():
    prompt = st.text_input("What would you like to know?", key="prompt")
    return prompt;

st.set_page_config(
    page_title="SQL Execution", page_icon="📊", layout="wide"
)
sql = set_up_sql.DatabaseManager()
#Create a connection to the database
for name, df in st.session_state.dataframes.items():
    sql.import_dtypes(st.session_state.column_types[name])
    sql.connect('sqlite:///NLP_SQL')
    sql.create_table(name, df)

sql.check_table_list()
sql.execute_query("Select customers.customer_id, orders.order_id from customers left join orders on customers.customer_id = orders.customer_id where customers.customer_id = '1';")

st.write("Which Result you would like to want?")
st.session_state.prompt_sentence = get_prompt()

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
