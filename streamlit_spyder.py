# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:18:25 2022

@author: Lenovo
"""

import streamlit as st
import pandas as pd


st.title("DATA ANALYSIS")
st.subheader("Data Analysis using python (in CSV format)")

upload = st.file_uploader("Upload your dataset (in CSV format)")
if upload is not None:
    data= pd.read_csv(upload)
    
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Show Head"):
            st.write(data.head())
        if st.button("Show Tail"):
            st.write(data.tail())
            
if upload is not None:
    if st.checkbox("Data Types of each column"):
        st.text("DataTypes")
        st.write(data.dtypes)
        
if upload is not None:
    data_shape=st.radio("What Dimension you would like to check?",('rows','columms'))
    
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

   
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("No Null Values detected")
        

# Finding Duplicate Values in the dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?", \
                         ("Select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
    
#  Getting Overall Statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))


#  About Section

if st.button("About App"):
    st.text("Built With ❤ by Ekta Agarwal")
    st.text("Libraries used- sreamlit/pandas/seaborn")



#  downloading 

if st.button('Save DataFrame'):
    open('data_streamlit.csv','w').write(data.to_csv())
    st.text("Saved To local Drive")
        
