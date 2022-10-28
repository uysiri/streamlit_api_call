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
st.info("For example, if your domain name is sageseo.ai, enter sageseo.ai into the box.")




# def get_data(data):
#         dt = requests.get(data).content
#         df = pd.read_csv(io.StringIO(dt.decode('utf-8')))
#         return pd.DataFrame(df)

@st.cache
def get_data(data):
#     dt = requests.get(data).content
    return pd.read_csv(data)

domain = st.text_input('Domain')
# domain = 'sageseo.ai'
if domain:
    try:
        url = 'https://b3z7u9yhxl.execute-api.us-east-1.amazonaws.com/dev/keywords/ranked?domain=' + domain + '&format=both'
        x = requests.get(url).json()
        xx=x['body']
        data = xx[0]
    except NameError:
        pass

# if 'body' in x:
#     xx=x['body']
#     data = xx[0]
# else:
#     st.write('There is no body in x')
 
if data:
    df = get_data(data)
    st.json(x)
    st.dataframe(df.head(50))
else:
    st.write("Get Started!")
   
# st.dataframe(df.head(50))
    
