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

    def date_type(self):
        for name, dataframe in st.session_state.dataframes.items():
            for col in dataframe.columns:
                if 'date' in col.lower(): # 컬럼 이름에 'date' 문자열이 포함되어 있는지 확인 (대소문자 구분 없음)
                    try:    
                        dataframe[col] = pd.to_datetime(dataframe[col]).dt.date
                        print(f"'{col}' 컬럼을 datetime 형식으로 변환했습니다.")
                    except Exception as e:
                        print(f"'{col}' 컬럼 변환 중 오류 발생: {e}")


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
    
    def create_table2(self, df_name, df):
        # Dataframe to SQLite
        df.to_sql(
            name=df_name,
            con=self.engine,          #self.dtype_dict is based on the data_types was selected manually.
            if_exists='replace',
            index=False
        )
        
    def execute_query(self, response):
        response = str(response).strip()
        st.write(f'This is the {response}')
        with self.engine.connect() as conn:
            self.result = conn.execute(text(f"{response}"))
            st.table(pd.DataFrame(self.result.all()))  # Display the result in Streamlit
        
    def check_table_list(self):
        inspector = inspect(self.engine)
        table_names = inspector.get_table_names()
        st.write(f"요런이름들 {table_names}")
        
    
