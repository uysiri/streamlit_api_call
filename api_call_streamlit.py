import json
import streamlit as st
import requests
import pandas as pd
import numpy as np
from http.client import HTTPSConnection
from base64 import b64encode
from json import loads
from json import dumps
import io
from io import StringIO
from PIL import Image

imurl = "https://i.imgur.com/BN924DB.png"
img = Image.open(requests.get(imurl, stream=True).raw)
st.image(img,width=300)


st.title('What Keywords Are You Ranked For?')
st.markdown("Find out by entering your domain name into the box below!")
st.info("For example, if your domain name is sageseo.ai, enter sageseo.ai into the box.")

@st.cache
def get_data(data):
    return pd.read_csv(data)

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

    
domain = st.text_input('Domain')
limit = st.radio(
    "What is the maximum number of ranked keywords you want to return?",
    ('10', '100', '1000'))
# if domain:
#     try:
#         url = 'https://b3z7u9yhxl.execute-api.us-east-1.amazonaws.com/dev/keywords/ranked?domain=' + domain + '&format=both&limit=100'
#         x = requests.get(url).json()
#         xx=x['body']
#         data = xx[0]
#         w = xx[1]
#         string = ",".join(str(e) for e in w)
#         newstr = string[9:]
#         df = get_data(data)
#         df.fillna(0, inplace=True)
#         for column in df.columns:
#             if df[column].dtype == 'float64':
#                 df[column] = df[column].astype(int)
#         st.write("Number of Ranked Keywords Returned:",len(df)-1)
#         st.write("Cost of API Call:",newstr.split(',', 1)[0])
#         st.dataframe(df)
#         csv = convert_df(df)
#         st.download_button(label="Download data as CSV", data=csv, file_name='sample_df.csv', mime='text/csv',)
#     except NameError:
#         pass
if (domain) and (limit == '10'):
    url = 'https://b3z7u9yhxl.execute-api.us-east-1.amazonaws.com/dev/keywords/ranked?domain=' + domain + '&format=both&limit=10'
    x = requests.get(url).json()
    xx=x['body']
    data = xx[0]
    df = get_data(data)
    df.fillna(0, inplace=True)
    for column in df.columns:
        if df[column].dtype == 'float64':
            df[column] = df[column].astype(int) 
    st.write(len(df)-1)
    st.dataframe(df)
    csv = convert_df(df)
    st.download_button(label="Download data as CSV", data=csv, file_name='sample_df.csv', mime='text/csv',)
elif (domain) and (limit == '100'):
    url = 'https://b3z7u9yhxl.execute-api.us-east-1.amazonaws.com/dev/keywords/ranked?domain=' + domain + '&format=both&limit=100'
    x = requests.get(url).json()
    xx=x['body']
    data = xx[0]
    df = get_data(data)
    df.fillna(0, inplace=True)
    for column in df.columns:
        if df[column].dtype == 'float64':
            df[column] = df[column].astype(int) 
    st.write(len(df)-1)
    st.dataframe(df)
    csv = convert_df(df)
    st.download_button(label="Download data as CSV", data=csv, file_name='sample_df.csv', mime='text/csv',)
elif (domain) and (limit == '1000'):
    url = 'https://b3z7u9yhxl.execute-api.us-east-1.amazonaws.com/dev/keywords/ranked?domain=' + domain + '&format=both&limit=1000'
    x = requests.get(url).json()
    xx=x['body']
    data = xx[0]
    df = get_data(data)
    df.fillna(0, inplace=True)
    for column in df.columns:
        if df[column].dtype == 'float64':
            df[column] = df[column].astype(int) 
    st.write(len(df)-1)
    st.dataframe(df)
    csv = convert_df(df)
    st.download_button(label="Download data as CSV", data=csv, file_name='sample_df.csv', mime='text/csv',)
else:
    st.write("no")
