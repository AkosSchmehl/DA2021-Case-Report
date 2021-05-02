# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:13:18 2021

@author: fenix9514
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar

data = pd.read_csv('netflix_titles.csv')

#Search for null values and drop them
data_null=data.isnull().sum()
#data.dropna(inplace=True)

#dropped these because they are irrelevant information
data = data.drop("show_id", axis= 1)
data = data.drop("cast", axis= 1)

#creating new year column from date_added column
data["year"] = data.date_added.apply(lambda x: str(x).split(",")[-1])

#most occuring date:2019
top_year = data.year.value_counts()

#most occuring country
top_country=data.country.value_counts()

#most occuring rating
top_rating = data.rating.value_counts()

#countries with most contribution to netflix content
contrib= data.country.value_counts().head(20)
plt.clf()

sns.set_style("whitegrid")
acontrib= sns.barplot(contrib.values,contrib.index)
acontrib.set_xlabel("Number of content")
plt.figure(figsize=(10,10))

#distribution of type of content on netflix 
plt.clf()
content= data.type.value_counts()
sns.countplot(x= "type",data= data)
plt.figure(figsize=(7,7))


#Number of content added on netflix over the years
plt.clf()
no_of_content= data.year.value_counts()
a_no_of_content= sns.lineplot(no_of_content.index,no_of_content.values)
a_no_of_content.set_ylabel("No of content")
plt.figure(figsize=(15,5))

#Movies by Genre
plt.clf()
movies = sns.countplot(x='listed_in',data=data, order = data['listed_in'].value_counts().head(10).index)
plt.xticks(rotation=45)
plt.figure(figsize=(16,8))
