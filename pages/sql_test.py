import set_up_sql
import streamlit as st
import pandas as pd
import sqlalchemy


sql = set_up_sql.DatabaseManager()
sql.date_type()
for name, df in st.session_state.dataframes.items():
    # sql.import_dtypes(st.session_state.column_types[name])
    sql.connect('sqlite:///NLP_SQL')
    sql.create_table2(name, df)

sql.execute_query('SELECT c.first_name, c.last_name FROM orders AS o JOIN customers AS c ON o.customer_id = c.customer_id GROUP BY c.customer_id ORDER BY COUNT(o.order_id) DESC LIMIT 1;')