import set_up_sql
import pandas as pd
import streamlit as st

sql = set_up_sql.DatabaseManager()
sql.import_dtypes('brands')
st.write(st.session_state.column_types['brands'])
sql.connect('sqlite:///brands')
sql.create_table('brands', st.session_state.dataframes['brands'])