#https://youtu.be/LZH_7PCpN2o

#obes-strmlt-hSbBZa94-py3.9
# from pickle import FALSE
#from tkinter import TRUE

from sqlalchemy import true
import streamlit as st
import pandas as pd

st.title("Streamlit Tutorial")

save_data = st.button("Save File")
df = pd.read_csv('names.csv')
st.header("DataFrame")
st.write(df)

st.sidebar.header("Options")

options_form = st.sidebar.form("GSEA NUmber")
gsea = options_form.text_input("GSEA Number")

gse_number = options_form.text_input("Gene Name")
LogFc = options_form.number_input("Log Fold Change")
add_data = options_form.form_submit_button()


# st.sidebar.subheader ("Remove Last added data")
# remove_last_added_data = options_form.form_submit_button()

if add_data:
    new_data = {'GSEA': gsea, 'Gene_name': gse_number, 'Log Fold Change': LogFc}
    df = df.append(new_data, ignore_index=True)
    df = df.to_csv('names.csv', index=False)

# if remove_last_added_data:
#     df = df.drop(df.tail(1).index)
#     df = df.to_csv('names.csv', index=False)

st.subheader("Updated Dataset")
df1 = pd.read_csv('names.csv')
st.write(df1.tail(5))

