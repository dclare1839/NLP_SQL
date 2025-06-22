import pandas as pd
import streamlit as st

class Description:

    def __init__(self):
        pass

    def describe_data(self, key, value):
        """
        Generate a description of the DataFrame.
        """
        self.description = value.describe(include='all').transpose()

        st.write(f"The file is '{key}'.")
        st.write("Data Head like below:")
        st.dataframe(value.head())
        st.dataframe(value.dtypes)
    
