#https://youtu.be/LZH_7PCpN2o

#obes-strmlt-hSbBZa94-py3.9
# from pickle import FALSE
#from tkinter import TRUE

from sqlalchemy import true
import streamlit as st
import pandas as pd

from streamlit_lottie import st_lottie
import json
st.title("Streamlit Tutorial")

@st.cache(allow_output_mutation=True)
def load_lottifile(filepath: str):
        with open(filepath, 'r') as f:
            return json.load(f)
loti_path = load_lottifile('data.json')
#st.title('Lotti')
with st.sidebar:
    
    #time.sleep(3)
    st_lottie(loti_path, width=280, height=180, loop=False)

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

# import matplotlib.pyplot as plt

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)

