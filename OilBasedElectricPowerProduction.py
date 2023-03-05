#!/usr/bin/env python
# coding: utf-8

# Name: Muhammad Ali
# 
# ID: 21069608

# # Loading Modules & Data

# In[1]:


# Importing related modules
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading dataset file
df = pd.read_csv("API_EG.ELC.PETR.ZS_DS2_en_csv_v2_4909772.csv", skiprows=4).iloc[:, :-1]
df.head()


# # Preparing Data for information

# In[ ]:


# FIlling missing values
df.fillna(0, inplace=True)


# In[2]:


# Extracting Valid countries data
import pycountry
countries = list(pycountry.countries)
country_names = [country.name for country in countries]

df = df[df["Country Name"].isin(country_names)]

