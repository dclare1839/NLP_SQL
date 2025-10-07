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
        pass
    
    def date_type(self):
        for name, dataframe in st.session_state.dataframes.items():
            for col in dataframe.columns:
                if 'date' in col.lower(): # To confirm whether the column name contains 'date'
                    try:    
                        dataframe[col] = pd.to_datetime(dataframe[col]).dt.date
                        print(f"'{col}' The type of column was converted to datetime.")
                    except Exception as e:
                        print(f"'{col}' There is an error during conversion: {e}")


    def connect(self,db_path):
        self.db_path = db_path
        self.engine = create_engine(self.db_path, echo=True)#Create a connection to the database

    #Create SQLite Table
    def create_table(self, df_name, df):
        # Dataframe to SQLite
        df.to_sql(
            name=df_name,
            con=self.engine, 
            if_exists='replace',
            index=False
        )
    
    #Execute SQL Query       
    def execute_query(self, response):
        response = str(response).strip()
        st.write(f'The query is {response}')
        with self.engine.connect() as conn:
            self.result = conn.execute(text(f"{response}"))
            st.table(pd.DataFrame(self.result.all()))  # Display the result in Streamlit
        
        
    
