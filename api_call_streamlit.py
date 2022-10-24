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

st.markdown("Input your domain name")
st.info("For example, if your domain name is pspost.co, enter 'pspost.co' into the box.")
domain = st.text_input('Domain')

# for input in domain:
#     try:
#         url = 'https://b3z7u9yhxl.execute-api.us-east-1.amazonaws.com/dev/keywords/ranked?domain=' + domain + '&format=both'
#         x = requests.get(url).json()
#         xx = x['body']
#     except NameError:
#         pass
        

# @st.experimental_memo
# @st.cache
# def reemovNestings(xx):
#     for i in xx:
#         if type(i) == list:
#             reemovNestings(i)

# xx = reemovNestings(xx)
# data = xx[0]

# @st.cache
# @st.experimental_memo
# def get_data(data):
#         dt = requests.get(data).content
# #         df = pd.read_csv(io.StringIO(dt.decode('utf-8')))
#         return dt
# get_data(data)    
# df = pd.read_csv(io.StringIO(dt.decode('utf-8')))

# @st.experimental_memo
# @st.cache
# def reemovNestings(xx):
#     for i in xx:
#         if type(i) == list:
#             reemovNestings(i)

for input in domain:
    try:
        url = 'https://b3z7u9yhxl.execute-api.us-east-1.amazonaws.com/dev/keywords/ranked?domain=' + domain + '&format=both'
        x = requests.get(url).json()
    except NameError:
        pass

if 'body' in x:
    xx=x['body']
#     xx = reemovNestings(xx)
    data = xx[0]
else:
    print('There is no body in x')
        

@st.cache
@st.experimental_memo
def get_data(data):
        dt = requests.get(data).content
        df = pd.read_csv(io.StringIO(dt.decode('utf-8')))
        return df
    
df = get_data(data)
    
st.dataframe(df)
    
