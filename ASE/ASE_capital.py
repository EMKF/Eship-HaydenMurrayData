# data dowmloaded manually from https://factfinder.census.gov/bkmk/table/1.0/en/ASE/2016/00CSCB08

import os
import sys
import time
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# load PEP data
df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_capital/ASE_2016_00CSCB08_with_ann.csv')

# keep vars
df = df[['GEO.display-label', 'NAICS.display-label', 'ASECB.display-label',\
         'YIBSZFI.display-label', 'ACQBUSCAP.display-label', 'FIRMPDEMP', 'FIRMPDEMP_PCT']]

# Rename columns
df.rename(columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECB.display-label": "demo",\
                   "YIBSZFI.display-label": "bus_age", "ACQBUSCAP.display-label": "startup_capital", "FIRMPDEMP": "count", "FIRMPDEMP_PCT": "percent"},inplace=True)

# filters
df = df[df['region'] == 'United States']
df = df[df['industry'] == 'Total for all sectors']
df = df[(df.demo == 'All firms') | (df.demo == 'Hispanic') | (df.demo == 'Black or African American')]
df = df[(df.bus_age == 'All firms')]

# reset index
df.reset_index(inplace=True, drop=True)
print(df)
df.to_excel('/Users/hmurray/Desktop/data/ASE/ASE_capital/ASE_cap.xlsx', index=False)

# sum categories
df['count'] = df['count'].astype(float)
cap_firms = df.iloc[1:10, 5].sum()
print(cap_firms)
df['count'] = df['count'].astype(float)
black_cap_firms = df.iloc[29:38, 5].sum()
print(black_cap_firms)
df['count'] = df['count'].astype(float)
hisp_cap_firms = df.iloc[15:24, 5].sum()
print(hisp_cap_firms)

# hisp plus black
hisp_black = black_cap_firms + hisp_cap_firms
print(hisp_black)

# percent black
per_black = (black_cap_firms/cap_firms)*100
print(per_black)

# percent hispanic
per_hisp = (hisp_cap_firms/cap_firms)*100
print(per_hisp)

# percent hispanic and black
per_black_hisp = (hisp_black/cap_firms)*100
print(per_black_hisp)

# tmp2 = tmp2.iloc[:,1:50].sum()
sys.exit()






