# data download: https://www2.census.gov/programs-surveys/acs/data/pums/2018/5-Year/
# data dictionary: https://www.census.gov/programs-surveys/acs/technical-documentation/pums/documentation.html

import pandas as pd
import matplotlib.pyplot as plt
import requests
import seaborn as ax
import numpy as np
import zipfile
import urlopen
from textwrap import wrap
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull in data
df = pd.read_csv('/Users/hmurray/Desktop/data/PUMS/p90_p10/csv_pmo/psam_p29.csv', low_memory=False,\
                 usecols=['SERIALNO', 'ST', 'PINCP', 'PERNP', 'ADJINC', 'COW', 'ESR', 'SEMP'])

# convert columns to lowercase
df.columns = map(str.lower, df.columns)

# drop working without pay in fam business and unemployed from worker status
# print(df['cow'].value_counts(dropna=False))
df = df[df.cow != 8]
df = df[df.cow != 9]

# create new column to recode class of worker
df['cow_recode'] = df['cow']
df['cow_recode'].replace({2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2}, inplace=True)

# recode to cow categories
cow_cats = {
    1: 'Employee',
    2: 'Self_Employed'
}

# replace age number with string
df["cow_recode"].replace(cow_cats, inplace=True)

# # inspect pincp and cow
# # print(df['cow_recode'].value_counts(dropna=False))
# print(df.head(250))
# df['pincp'].hist(bins=150, align='mid')
# plt.title('Histogram of Total Person\'s Income (PINCP) in MO')
# plt.show()

# calculate percentiles for all cow
print(df['pincp'].quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9]))
print(df['pincp'].mean())

# create unique ID column and unstack cow
df = df.reset_index()
df["id"] = df.index + 1
cow_df = df.pivot_table(index=['id', 'st'], columns='cow_recode', values='pincp')
print(cow_df.head())
cow_df.to_excel('/Users/hmurray/Desktop/data/PUMS/p90_p10/csv_pmo/mo_cow_table.xlsx', index=False)

# inspect cow income
print(cow_df['Employee'].quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9]))
print(cow_df['Employee'].mean())
print(cow_df['Self_Employed'].quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9]))
print(cow_df['Self_Employed'].mean())

# plot histograms for cow
## Employee
Employee = cow_df['Employee'].hist(bins=100, alpha=.3, align='mid', histtype='stepfilled', density=True)
Self_Employed = cow_df['Self_Employed'].hist(bins=100, alpha=.3, align='mid', histtype='stepfilled', density=True)
plt.title('Histograms of Self_Employed and Employed Income in MO')
plt.xlim(xmin=-10000, xmax = 300000)
# plt.legend([Employee, Self_Employed], ['Employee','Self_Employed'])
plt.savefig('/Users/hmurray/Desktop/data/PUMS/p90_p10/csv_pmo/mo_cow_hist.png')
plt.show()

sys.exit()