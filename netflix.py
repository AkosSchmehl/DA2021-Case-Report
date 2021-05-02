# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:13:18 2021

@author: fenix9514
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# we need the calendar module for this one
import calendar

data = pd.read_csv('netflix_titles.csv')

data = data.drop("show_id", axis=1)
data = data.drop("date_added", axis=1)
data = data.drop("cast", axis=1)

data.dropna(inplace=True)