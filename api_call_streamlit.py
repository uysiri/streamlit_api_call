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
st.image(img,width=400)

st.markdown("Input your domain name")
st.info("For example, if your domain name is pspost.co, enter 'pspost.co' into the box.")
domain = st.text_input('Domain')

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

# @st.cache
# @st.experimental_memo
# def get_data(data):
#         dt = requests.get(data).content
#         df = pd.read_csv(io.StringIO(dt.decode('utf-8')))
#         return df
# @st.experimental_memo

@st.cache
def get_data():
    dt = requests.get(data).content
    return pd.read_csv(io.StringIO(dt.decode('utf-8')))

# def get_data(data):
#         dt = requests.get(data).content
#         df = pd.read_csv(io.StringIO(dt.decode('utf-8')))
#         return pd.DataFrame(df)

for input in domain:
    try:
        url = 'https://b3z7u9yhxl.execute-api.us-east-1.amazonaws.com/dev/keywords/ranked?domain=' + domain + '&format=both'
        x = requests.get(url).json()
    except NameError:
        pass

if 'body' in x:
    xx=x['body']
    data = xx[0]
else:
    st.write('There is no body in x')
            
df = get_data()    
st.dataframe(df)
    
