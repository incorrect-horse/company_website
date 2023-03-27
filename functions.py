import streamlit as st


def build_cols(df, col, range_start, range_end):
    with col:
        for index, row in df[range_start:range_end].iterrows():
            st.subheader(f'{row["first name"].strip().title()} {row["last name"].strip().title()}')
            st.write(row["role"])
            st.image("images/" + row["image"])
    return index
