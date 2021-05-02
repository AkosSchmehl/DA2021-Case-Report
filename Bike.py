# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:21:50 2021

@author: fenix9514
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# we need the calendar module for this one
import calendar
from scipy import stats

# our helper function to create the price difference
# between selling price and present price (ex-showroom price)
def percentage_difference(row):
    selling = row['selling_price']
    present = row['ex_showroom_price']

    # the difference in decimal format
    result = 1 - round(selling / present, 2)
    return result
 
pd.set_option('display.float_format', lambda x: '%.1f' % x)
bikes = pd.read_csv('BIKE DETAILS.csv')

bikes = bikes.drop(bikes[bikes.ex_showroom_price > 999999].index)

#highest_original=bikes["ex_showroom_price"].max()

 
bikes['price_difference'] = bikes.apply(percentage_difference, axis=1)
 
 
#owner is not relevant
#bikes = bikes.drop('owner', axis=1)
bikes = bikes.drop('seller_type', axis=1)


#fill showroom price and difference with averages
bikes['ex_showroom_price'].fillna((bikes['ex_showroom_price'].mean()), inplace=True)
bikes['price_difference'].fillna((bikes['price_difference'].mean()), inplace=True)

lowest_price=bikes["selling_price"].min()
highest_price=bikes["selling_price"].max()

group_year =  bikes.groupby('year').count()


#number of bikes sold by name
groupbyname = bikes.groupby('name').count()
groupbyname = groupbyname.drop('selling_price', axis=1)
groupbyname = groupbyname.drop('km_driven', axis=1)
groupbyname = groupbyname.drop('year', axis=1)
groupbyname = groupbyname.drop('ex_showroom_price', axis=1)
groupbyname = groupbyname.drop('price_difference', axis=1)

#most sold bike is bajaj pulsar 150
mostsoldbike=groupbyname.loc[groupbyname['owner'].idxmax()]
print(mostsoldbike)

#top 3 most sold bikes are from bajaj, REC, Honda
most_common_bikes = bikes["name"].value_counts()[:3].index.tolist()


correlations = bikes.corr()


plt.clf()
sns.pairplot(bikes)
plt.figure()
 
plt.clf()
sns.distplot(bikes['year'])
plt.figure()

plt.clf()
sns.distplot(bikes['price_difference'])
plt.figure()


#plt.clf()
#sns.barplot(x='km_driven', y='selling_price', data=bikes)
#plt.figure()

#there was a huge spike in selling price