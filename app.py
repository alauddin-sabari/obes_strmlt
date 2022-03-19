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

options_form = st.sidebar.form("x")
disease = options_form.text_input("DISEASE NAME")

gse_number = options_form.text_input("GSE NUMBER")
src = options_form.number_input("Data Source")
src_link = options_form.number_input("Source link(Optional)")

add_data = options_form.form_submit_button()


# st.sidebar.subheader ("Remove Last added data")
# remove_last_added_data = options_form.form_submit_button()

if add_data:
    new_data = {'DISEASE NAME': disease, 'GSE NUMBER': gse_number, 'Data Source': src, 'Source link(Optional)': src_link}
    df = df.append(new_data, ignore_index=True)
    df = df.to_csv('names.csv', index=False)

# if remove_last_added_data:
#     df = df.drop(df.tail(1).index)
#     df = df.to_csv('names.csv', index=False)

st.subheader("Updated Dataset")
df1 = pd.read_csv('names.csv')
st.write(df1.tail(5))

