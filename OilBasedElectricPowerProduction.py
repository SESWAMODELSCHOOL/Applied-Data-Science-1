#!/usr/bin/env python
# coding: utf-8

# Name: Muhammad Ali

# ID: 21069608

# # Loading Modules & Data


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

# FIlling missing values
df.fillna(0, inplace=True)
dn.fillna(0, inplace=True)

# Extracting Valid countries data
import pycountry
countries = list(pycountry.countries)
country_names = [country.name for country in countries]

df = df[df["Country Name"].isin(country_names)]
dn = dn[dn["Country Name"].isin(country_names)]


# Dropping all related world records

index = df[df["Country Name"] == "World"].index
index = dn[dn["Country Name"] == "World"].index
df.drop(index, axis=0, inplace=True)
dn.drop(index, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
dn.reset_index(drop=True, inplace=True)

# # Visualizations of data in different forms

#  1. line Graph of Electric power production on Oil vs Nuclear energy

# sorting, manipulating and labeling data
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
    
#   2. Coding for Bar Graph

# setting range and sorting data for comparision

temp = df_oil.iloc[:, 20:].mean(axis=1).sort_values(ascending=False)
nuc = dn_ncl.iloc[:, 20:].mean(axis=1).sort_values(ascending=False)
temp = temp[temp > 0][0:10]
nuc = nuc[nuc > 0][0:10]
plt.figure(figsize=(15, 12))
plt.subplot(2,2 ,1)
ol=sns.barplot(temp.index, temp.values)
plt.title("Top 10 Countries with Highest Oil-based electricty production", fontsize=12)
plt.xticks(rotation= 70)
plt.xlabel(" Country Name ")
plt.ylabel("%age Electic Energy Oil based")
plt.subplot(2,2 ,2)
nl=sns.barplot(nuc.index, nuc.values)
plt.title("Top 10 Countries with Highest Nuclear based Electricity Production", fontsize=12)
plt.xticks(rotation=70)
plt.xlabel(" Country Name ")
plt.ylabel("%age Electric Energy Nuclear based")

plt.show()

# 3. Coding for Pie Graphs

# setting parameters and fix limits for data ploting

temp = df_oil.mean()
nl = dn_ncl.mean()
temp = temp[temp>0][20:60]
nl = nl[nl>0][20:60]
plt.figure(figsize=(15,15))
plt.subplot(2,2 ,1)
plt.pie(temp.values, labels=temp.index)
plt.title("Electricity Production Per Year From Nuclear Energy 1980-2015")
plt.subplot(2,2 ,2)
plt.pie(nl.values, labels=nl.index)
plt.title("Electricity Production Per Year From Oil Sources 1980-2015")
plt.show()

