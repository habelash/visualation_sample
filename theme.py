import streamlit as st
import pandas  as pd


st.write("""
# Visualation
## *Theme*
""")

df = pd.read_csv('data.csv')

st.bar_chart(df)