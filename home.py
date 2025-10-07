import pandas as pd
import streamlit as st
import description # Description module

# Prompt to some description which sql code you would like to generate

if "dataframes" not in st.session_state:
    # 'dataframes'는 여러 데이터프레임을 저장하는 딕셔너리 형태일 가능성이 높으므로,
    # 빈 딕셔너리로 초기화하는 것이 일반적입니다.
    st.session_state["dataframes"] = {} 

# Set up the title of Streamlit app
st.set_page_config(page_title="Data Analysis App", page_icon="📊", layout="wide")

# Set up the sidebar
st.session_state.gemini_api_key = st.sidebar.text_input(
    "Enter your Gemini API Key",
    type="password"  #Hide the input for security
)
# Set up some layout for main page
st.title("Database Analysis Procedure")

st.markdown(
    body='''
        ## Purpose \n 
        1. Analyzing the database with Natural Language Programming (NLP) \n
        2. Recommend what kinds of analysis you can try from this app. \n
        3. Visualize what you would like to see. \n

'''
)

st.divider()
