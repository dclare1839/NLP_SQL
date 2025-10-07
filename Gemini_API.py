import google.generativeai as genai
import os
import streamlit as st

class geminiAPI:
    def __init__(self):
        #with open('/Users/aiden/Desktop/NLP_SQL_Outfolder/API_KEY.txt', 'r') as file:
        #    self.APIK = file.read()
        self.APIK = st.session_state.gemini_api_key
        
        self.response = 'example response'  # Initialize response variable
        self.buffer = []  # Initialize buffer for streaming response

    def configure(self): #Gemini API Connect
        genai.configure(api_key=self.APIK)
        self.model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
        #Gemini-2.5-flash version is available in Gemini API Free Tier version.
    

    def generate_sql_query(self, prompt, prompt_settings):
        if prompt:  # Only generate if prompt is not empty

            # Creating an environment for database
            db_settings = ""
            for name, columns in prompt_settings.items(): # Inputting all the names of files and columns to get the exact SQL code from Gemini
                db_settings += f"The name of table is {name} and columns are {columns.to_list()}. "

            # Prompt Basis to get accurate answer
            sql_prompt = f"""
            Based on these columns: {db_settings}
            Generate ONLY the SQL query for: {prompt}
            
            Return only the SQL code without any explanation or formatting.
            """
            self.response = self.model.generate_content(sql_prompt) #Run Gemini
            
            self.buffer = []
            for chunk in self.response:
                self.buffer.append(chunk.text) # Extracting required results
            
            self.result = ''.join(self.buffer)[7:-4] # Cleaning the result to get only SQL code
            return self.result
    