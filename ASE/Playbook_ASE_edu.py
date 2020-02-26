# data dowmloaded manually from https://factfinder.census.gov/bkmk/table/1.0/en/ASE/2016/00CSCBO07

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
df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_edu/ASE_2016_00CSCBO07_with_ann.csv')

# keep vars
df = df[['GEO.display-label', 'NAICS.display-label', 'ASECBO.display-label',\
         'YIBSZFI.display-label', 'EDUC.display-label', 'OWNPDEMP', 'OWNPDEMP_PCT']]

# Rename columns
df.rename(columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECBO.display-label": "demo",\
                   "YIBSZFI.display-label": "bus_age", "EDUC.display-label": "edu", "OWNPDEMP": "count", "OWNPDEMP_PCT": "percent"},inplace=True)

# filters
df = df[df['region'] == 'United States']
df = df[df['industry'] == 'Total for all sectors']
df = df[(df.demo == 'All owners of respondent firms') | (df.demo == 'Minority') | (df.demo == 'Nonminority')]
df = df[(df.bus_age == 'All firms')]

# reset index
df.reset_index(inplace=True, drop=True)
print(df)
df.to_excel('/Users/hmurray/Desktop/data/ASE/ASE_edu/ASE_edu_minorities.xlsx', index=False)

# percent all firms with less than HS
less_hs = df.iloc[0,6]
less_hs_count = df.iloc[0,5]
print(less_hs)

min_less_hs = df.iloc[9,6]
min_less_hs_count = df.iloc[9,5]
print(min_less_hs)

# percent with no more than HS degree
all_hs = df.iloc[1,6]
all_hs = int(float(all_hs))


min_hs = df.iloc[10,6]
min_hs = int(float(min_hs))

all_plus = less_hs + all_hs
min_plus = min_less_hs + min_hs

print(all_plus)
print(min_plus)

