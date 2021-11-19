# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
import numpy as np

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Topic Title](#Topic-Title)
# + [Topic 2 Title](#Topic-2-Title)

# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide. 

#

# ## Contents
# + [Processing Time Data](#Processing-Time-Data)
# + [Topic 2 Title](#Topic-2-Title)

# * ###  Processing Time Data
#
# **Yurui Chang**

# #### Pandas.to_timedelta
#
# - To convert a recognized timedelta format / value into a Timedelta type
# - the unit of the arg
#   * 'W'
#   * 'D'/'days'/'day'
#   * ‘hours’ / ‘hour’ / ‘hr’ / ‘h’
#   * ‘m’ / ‘minute’ / ‘min’ / ‘minutes’ / ‘T’
#   * ‘S’ / ‘seconds’ / ‘sec’ / ‘second’
#   * ‘ms’ / ‘milliseconds’ / ‘millisecond’ / ‘milli’ / ‘millis’ / ‘L’
#   * ‘us’ / ‘microseconds’ / ‘microsecond’ / ‘micro’ / ‘micros’ / ‘U’
#   * ‘ns’ / ‘nanoseconds’ / ‘nano’ / ‘nanos’ / ‘nanosecond’ / ‘N’

# * Parsing a single string to a Timedelta
# * Parsing a list or array of strings
# * Converting numbers by specifying the unit keyword argument

time1 = pd.to_timedelta('1 days 06:05:01.00003')
time2 = pd.to_timedelta('15.5s')
print([time1, time2])
pd.to_timedelta(['1 days 06:05:01.00003', '15.5s', 'nan'])

pd.to_timedelta(np.arange(5), unit='d')

# #### pandas.to_datetime
#
# * To convert argument to datetime
# * Returns: datetime, return type dependending on input
#   * list-like: DatetimeIndex
#   * Series: Series of datetime64 dtype
#   * scalar: Timestamp
# * Assembling a datetime from multiple columns of a DataFrame
# * Converting Pandas Series to datetime w/ custom format
# * Converting Unix integer (days) to datetime
# * Convert integer (seconds) to datetime

s = pd.Series(['date is 01199002',
           'date is 02199015',
           'date is 03199020',
           'date is 09199204'])
pd.to_datetime(s, format="date is %m%Y%d")

time1 = pd.to_datetime(14554, unit='D', origin='unix')
print(time1)
time2 = pd.to_datetime(1600355888, unit='s', origin='unix')
print(time2)


# # Title: Pandas Time Series Analysis
# ## Name: Kenan Alkiek (kalkiek)

import pandas as pd
from matplotlib import pyplot as plt

# Read in the air quality dataset
air_quality = pd.read_csv(
    'https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/air_quality_no2_long.csv')
air_quality["datetime"] = pd.to_datetime(air_quality["date.utc"])

# One common method of dealing with time series data is to set the index equal to the data
air_quality = air_quality.set_index('datetime')
air_quality.head()

# Plot the NO2 Over time for Paris france
paris_air_quality = air_quality[(air_quality['city'] == 'Paris') & (air_quality['country'] == 'FR')]

paris_air_quality.plot()
plt.ylabel("$NO_2 (µg/m^3)$")

# Plot average NO2 by hour of the day
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby("date.utc")["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
plt.show()

# Limit the data between 2 dates
beg_of_june = paris_air_quality["2019-06-01":"2019-06-03"]
beg_of_june.plot()
plt.ylabel("$NO_2 (µg/m^3)$")

# Resample the Data With a Different Frequency (and Aggregration)
monthly_max = air_quality.resample("M").max()
print(monthly_max)

# Ignore weekends and certain times
rng = pd.date_range('20190501 09:00', '20190701 16:00', freq='30T')

# Grab only certain times
rng = rng.take(rng.indexer_between_time('09:30', '16:00'))

# Remove weekends
rng = rng[rng.weekday < 5]

rng.to_series()


# ## Pivot Table in pandas
#
#
# *Mingjia Chen* 
# mingjia@umich.edu

# - A pivot table is a table format that allows data to be dynamically arranged and summarized in categories.
# - Pivot tables are flexible, allowing you to customize your analytical calculations and making it easy for users to understand the data.
# - Use the following example to illustrate how a pivot table works.

# +
import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [1, 2, 3, 4, 5],
                   "B": [0, 1, 0, 1, 0],
                   "C": [1, 2, 2, 3, 3],
                   "D": [2, 4, 5, 5, 6],
                   "E": [2, 2, 4, 4, 6]})
print(df)
# -

# ## Index
#
# - The simplest pivot table must have a data frame and an index.
# - In addition, you can also have multiple indexes.
# - Try to swap the order of the two indexes, the data results are the same.

tab1 = pd.pivot_table(df,index=["A"])
tab2 = pd.pivot_table(df,index=["A", "B"])
tab3 = pd.pivot_table(df,index=["B", "A"])
print(tab1)
print(tab2)
print(tab3)

# ## Values 
# - Change the values parameter can filter the data for the desired calculation.

pd.pivot_table(df,index=["B", "A"], values=["C", "D"])

# ## Aggfunc
#
# - The aggfunc parameter sets the function that we perform when aggregating data.
# - When we do not set aggfunc, it defaults aggfunc='mean' to calculate the mean value.
#   - When we also want to get the sum of the data under indexes:

pd.pivot_table(df,index=["B", "A"], values=["C", "D"], aggfunc=[np.sum,np.mean])

# ## Columns
#
# - columns like index can set the column hierarchy field, it is not a required parameter, as an optional way to split the data.
#
# - fill_value fills empty values, margins=True for aggregation

pd.pivot_table(df,index=["B"],columns=["E"], values=["C", "D"],
               aggfunc=[np.sum], fill_value=0, margins=1)
