import streamlit as st
import pandas
from functions import build_cols

print("Script start...")


st.set_page_config(layout="wide")

st.header("The Best Company")

st.write("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed 
    do eiusmod tempor incididunt ut labore et dolore magna 
    aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
    ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis 
    aute irure dolor in reprehenderit in voluptate velit esse 
    cillum dolore eu fugiat nulla pariatur. Excepteur sint 
    occaecat cupidatat non proident, sunt in culpa qui officia 
    deserunt mollit anim id est laborum.
    """)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("files/data.csv", sep=",")

count_rows = 0
for index, row in df.iterrows():
    count_rows += 1

rows_to_col = count_rows // 3 #floor division

rows_col1 = rows_to_col
rows_col2 = rows_to_col + rows_col1
rows_col3 = rows_to_col + rows_col2

if count_rows / 3 != count_rows // 3:
    rows_col1 += 1
    rows_col2 += 2
    rows_col3 += 3

build_cols(df, col1, 0, int(rows_col1))
build_cols(df, col2, int(rows_col1), int(rows_col2))
build_cols(df, col3, int(rows_col2), int(rows_col3))
