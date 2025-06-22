NLP SQL Code Extraction System
This document outlines the architecture and key components of a system designed to extract SQL code from natural language queries, leveraging Streamlit for the user interface, Gemini API for SQL generation, and SQLite with SQLAlchemy for data management.

1. Overview
The NLP SQL Code Extraction System allows users to upload CSV files, define their data schema, input natural language queries, and receive executable SQL code and query results. It aims to bridge the gap between business users and database interactions by enabling SQL generation through intuitive natural language.

2. System Components
I. User Interface (Streamlit Application)
CSV File Upload: Provides an interface for users to upload CSV files, with initial data previews.

Data Schema Definition: Allows users to view column names and select appropriate data types for each column. Optional field for general dataset description.

Natural Language Query Input: A text field for users to input their desired query in natural language.

Results Display & Management: Shows the generated SQL code, query results in a table format, error messages, and options to download results (CSV/Excel) or submit additional queries.

II. Core Logic (Python Backend)
Data Processing Module: Handles CSV parsing, conversion to Pandas DataFrames, and mapping Streamlit-selected data types to SQLAlchemy-compatible types.

Gemini API Integration: Prepares API calls with user queries, schema information, and descriptions. Processes API responses to extract generated SQL code and performs basic validation.

Database Management (SQLAlchemy & SQLite): Sets up SQLAlchemy engine/connection, creates in-memory or temporary SQLite databases, loads Pandas DataFrames into SQLite tables (respecting specified column types), executes generated SQL queries, and returns results as Pandas DataFrames.

III. External Service (Gemini API)
Natural Language Understanding & SQL Generation: Analyzes user queries and leverages provided schema and descriptions to generate optimal SQL queries.

Response Format: Returns the generated SQL code.

3. Data Flow
The system follows a clear data flow:
CSV Input → Streamlit → SQLite → Gemini API → SQL → SQLite → Streamlit Output

4. User Experience
The system is designed with a focus on:
Intuitive UI/UX
Clear error feedback
Fast result retrieval
