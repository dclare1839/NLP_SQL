import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, Date, Time
import ast
import pandas as pd
import streamlit as st

class DatabaseManager():

    def __init__(self):
        self.dtype_dict = {
            'Country': String(50),
            'Year': Integer,
            'AttackType': String(100),
            'Industry': String(100),
            'Loss': Float,
            'Number_Users': Integer,
            'Source': String(50),
            'Vulnerability': String(100),
            'DefenseMechanism': String(100),
            'ResolutionTime': Integer
        }

    def connect(self,db_path):
        self.db_path = db_path
        self.engine = create_engine(self.db_path, echo=True)#Create a connection to the database

    def create_table(self, df):
        df.to_sql(
            name='cyber_security',
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
        
        
    
