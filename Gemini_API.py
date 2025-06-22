import google.generativeai as genai
import os
import streamlit as st
from IPython.display import Markdown, clear_output, display
import json

# for model in genai.list_models():
#     print(f"Model: {model.name}")
#     print(f"Display Name: {model.display_name}")
#     print("---")

class geminiAPI:
    def __init__(self):
        with open('/Users/aiden/Desktop/NLP_SQL_Outfolder/API_KEY.txt', 'r') as file:
            self.APIK = file.read()
        
        # with open("/Users/aiden/Desktop/NLP_SQL/prompt_setting.txt", 'r') as file:
        #     self.prompt_setting = file.read()
        
        self.response = 'example response'  # Initialize response variable
        self.buffer = []  # Initialize buffer for streaming response

    def import_db_columns(self, db_columns):
        self.db_columns = db_columns  # Update the database columns

    def configure(self):
        genai.configure(api_key=self.APIK)
        self.model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
    

    def create_sql_query(self, prompt):
        if prompt:  # Only generate if prompt is not empty
            
            # with open("/Users/aiden/Desktop/NLP_SQL/prompt_setting.txt", 'r') as file:
            #     self.data_description = file.read()

            # SQL만 요청하는 프롬프트
            sql_prompt = f"""
            the table name is 'cyber_security'.
            Based on these columns: {st.session_state.dataframes.items()}
            Generate ONLY the SQL query for: {prompt}
            
            Return only the SQL code without any explanation or formatting.
            """
            self.response = self.model.generate_content(sql_prompt)
            
            self.buffer = []
            for chunk in self.response:
                self.buffer.append(chunk.text)
            
            st.write(f"Response from the model: {''.join(self.buffer)[7:]}")
            self.result = ''.join(self.buffer)[7:-4]
            return self.result
    
    def recom_dtypes(self, df):
        self.dtype_format = """
Please provide data types in dictionary format. based on its name, please assume the data format.
Example:
{
    "product_id": Integer,
    "product_name": String(255),
    "order_date": Date
}
return only the data types in dictionary format without any other comments.
"""
        self.response = self.model.generate_content(f"{self.dtype_format}, and please recommend me the appropriate datatypes based on {df.describe()}.")

        self.buffer = []
        for chunk in self.response:
            self.buffer.append(chunk.text)
        self.response_text = "".join(self.buffer)

        try:
            # 마크다운 코드 블록 제거 (```json ... ```)
            if self.response_text.startswith("```json") and self.response_text.endswith("```"):
                json_string = self.response_text[7:-3].strip()
            else:
                json_string = self.response_text.strip()
            
            parsed_data = json.loads(json_string)
        except json.JSONDecodeError as e:
            print(f"JSON 파싱 오류: {e}")
            print(f"원시 응답: {self.response_text}")
            return {} # 또는 적절한 오류 처리

        return parsed_data
