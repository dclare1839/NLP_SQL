import google.generativeai as genai
import os
import streamlit as st
from IPython.display import Markdown, clear_output, display

# for model in genai.list_models():
#     print(f"Model: {model.name}")
#     print(f"Display Name: {model.display_name}")
#     print("---")

class geminiAPI:
    def __init__(self):
        with open('/Users/aiden/Desktop/NLP_SQL/API_KEY.txt', 'r') as file:
            self.APIK = file.read()
        
        with open("/Users/aiden/Desktop/NLP_SQL/prompt_setting.txt", 'r') as file:
            self.prompt_setting = file.read()
        
        self.response = 'example response'  # Initialize response variable
        self.buffer = []  # Initialize buffer for streaming response

    def import_db_columns(self, db_columns):
        self.db_columns = db_columns  # Update the database columns

    def configure(self):
        genai.configure(api_key=self.APIK)
        self.model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
    

    def create_sql_query(self, prompt):
            if prompt:  # Only generate if prompt is not empty
                
                with open("/Users/aiden/Desktop/NLP_SQL/prompt_setting.txt", 'r') as file:
                    self.data_description = file.read()

                # SQL만 요청하는 프롬프트
                sql_prompt = f"""
                the table name is 'cyber_security'.
                Based on these columns: {self.db_columns}
                Generate ONLY the SQL query for: {prompt}
                
                Return only the SQL code without any explanation or formatting.
                """
                self.response = self.model.generate_content(sql_prompt)
               
                self.buffer = []
                for chunk in self.response:
                    self.buffer.append(chunk.text)
                    clear_output()
                
                #st.write(f"Response from the model: {''.join(self.buffer)[7:]}")