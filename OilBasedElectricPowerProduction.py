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
dn = pd.read_csv("API_EG.ELC.NUCL.ZS_DS2_en_csv_v2_4912367.csv", skiprows=4).iloc[:, :-1]
df.head()
dn.head()

# # Preparing Data for information

# In[ ]:


# FIlling missing values
df.fillna(0, inplace=True)
dn.fillna(0, inplace=True)

# In[2]:


# Extracting Valid countries data
import pycountry
countries = list(pycountry.countries)
country_names = [country.name for country in countries]

df = df[df["Country Name"].isin(country_names)]
dn = dn[dn["Country Name"].isin(country_names)]

# In[3]:


# Dropping all related world records
index = df[df["Country Name"] == "World"].index
index = dn[dn["Country Name"] == "World"].index
df.drop(index, axis=0, inplace=True)
dn.drop(index, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
dn.reset_index(drop=True, inplace=True)

# # Visualizations of data in different forms

#  1. line Graph of Electric power production on Oil vs Nuclear energy

# In[4]:


unwanted_cols = ["Country Code", "Indicator Name", "Indicator Code"]
useless_cols=["Country Code", "Indicator Name", "Indicator Code"]
df_oil = df.drop(unwanted_cols, axis=1).set_index("Country Name").iloc[:, :-2]
dn_ncl = dn.drop(useless_cols, axis=1).set_index("Country Name").iloc[:, :-2]
df_oil.iloc[:, 20:55].mean().plot(kind="line", figsize=(15, 6),label="Oil Based")
dn_ncl.iloc[:, 20:55].mean().plot(kind="line", figsize=(15, 6), label="Nuclear Based")
plt.title("Percentage Electricty Production on Oil vs Nuclear resources in the whole World", fontsize=18)
plt.xlabel("Year", fontsize=15)
plt.ylabel("Percentage ", fontsize=15)
plt.legend()
plt.show()

