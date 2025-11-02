# 🧩 NLP → SQL Code Extraction System

This project demonstrates an end-to-end **Natural Language to SQL Generation System**, designed to help users query structured datasets without writing SQL manually.  
It connects uploaded CSV files to a lightweight database and generates SQL queries automatically through an AI model (Gemini API).

---

## 🚀 Overview

The **NLP_SQL System** bridges the gap between **business users** and **database systems**.  
By combining natural language processing (NLP) and SQL execution, it allows non-technical users to extract insights directly from their data.

**Example:**  
> “Show me the total sales by region in 2024” → Automatically converted into an executable SQL query.

---

## 🧱 System Architecture

| Component | Description |
|------------|-------------|
| **Frontend (Streamlit)** | Web-based UI for CSV upload, schema setup, and query input |
| **Backend (Python)** | Handles CSV parsing, schema inference, API communication, and database management |
| **Database (SQLite + SQLAlchemy)** | In-memory database for running dynamically generated queries |
| **AI Model (Gemini API)** | Converts natural language into syntactically valid SQL statements |

**Data Flow:**  
`CSV Upload → Streamlit → Gemini API → SQL Generation → SQLite Query → Streamlit Output`

---

## ⚙️ Core Functionalities

- 📂 **CSV File Upload & Preview**  
  Users can upload CSV datasets and inspect the first few rows.

- 🧾 **Automatic Schema Detection**  
  The system detects column names and lets users define data types.

- 💬 **Natural Language Query Interface**  
  Input your question in plain English — the system will interpret and translate it into SQL.

- 🧠 **AI-driven SQL Generation**  
  Uses the Gemini API to understand user intent and output optimized SQL code.

- 📊 **Interactive Results**  
  Displays query results in tables, with download options (CSV / Excel).

---

## 🧩 Example Workflow

1. Upload a dataset: `sales_data.csv`
2. Define column types (`date`, `region`, `sales_amount`)
3. Input question:  
   > “Show average monthly sales for each region”
4. The system generates:  
   ```sql
   SELECT region, AVG(sales_amount) AS avg_sales
   FROM sales_data
   GROUP BY region;
