import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, Date, Time
from sqlalchemy import inspect
import ast
import pandas as pd
import streamlit as st

class DatabaseManager():

    def __init__(self):
        self.sql_dict = {
            "String(200)":String(200),
            "Integer":Integer,
            "Float":Float,
            "Boolean":Boolean,
            "Date":Date,
            "Datetime":DateTime
        }

    def import_dtypes(self, column_types):
        self.dtype_dict = { column:self.sql_dict[types] for column, types in column_types.items()}



    def connect(self,db_path):
        self.db_path = db_path
        self.engine = create_engine(self.db_path, echo=True)#Create a connection to the database

    #Create SQLite Table
    def create_table(self, df_name, df):
        df.to_sql(
            name=df_name,
            con=self.engine,
            dtype=self.dtype_dict,           # 데이터 타입 지정
            if_exists='replace',
            index=False
        )
    
    def execute_query(self, response):
        response = str(response).strip()
        st.write(response)
        with self.engine.connect() as conn:
            self.result = conn.execute(text(f'{response}'))
            st.table(pd.DataFrame(self.result.all()))  # Display the result in Streamlit
        
    def check_table_list(self):
        inspector = inspect(self.engine)
        table_names = inspector.get_table_names()
        st.write(f"요런이름들 {table_names}")
        
    
