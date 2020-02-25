# data downloaded manually from https://factfinder.census.gov/bkmk/table/1.0/en/ASE/2016/00CSA04

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
df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_employ/ASE_2016_00CSA04_with_ann.csv')

# keep vars
df = df[['GEO.display-label', 'NAICS.display-label', 'SEX.display-label', 'ETH_GROUP.display-label',\
         'RACE_GROUP.display-label','VET_GROUP.display-label', 'EMPSZFI.display-label', 'FIRMPDEMP']]

# Rename columns
df.rename(columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "SEX.display-label": "sex"\
    ,"ETH_GROUP.display-label": "ethnicity", "RACE_GROUP.display-label": "race", "VET_GROUP.display-label": "vet",\
                   "EMPSZFI.display-label": "employ", "FIRMPDEMP": "count"},inplace=True)

# filters
df = df[df['region'] == 'United States']
df = df[df['industry'] == 'Total for all sectors']
df = df[df['sex'] == 'All firms']
df = df[df['ethnicity'] == 'All firms']
df = df[df['vet'] == 'All firms']
df = df[(df.race == 'All firms') | (df.race == 'Minority') | (df.race == 'Nonminority')]

# reset index
df.reset_index(inplace=True, drop=True)
print(df)
df.to_excel('/Users/hmurray/Desktop/data/ASE/ASE_employ/all_min_nonmin_employ.xlsx')

# percent minority firms
all = df.iloc[0,7]
all = int(all)

min = df.iloc[10,7]
min = int(min)

per_min = (min/all)*100
print(per_min)

# percent minority firms with 250+ employees
sum_250 = df.iloc[8,7]
sum_250 = int(sum_250)

min_sum_250 = df.iloc[18,7]
min_sum_250 = int(min_sum_250)

all_500 = df.iloc[9,7]
all_500 = int(all_500)

min_500 = df.iloc[19,7]
min_500 = int(min_500)

all_plus = sum_250 + all_500
min_plus = min_sum_250 + min_500

per_250 = (min_plus/all_plus)*100
print(all_plus)
print(min_plus)
print(per_250)

# percent minority firms with 500+ employees
firms500 = df.iloc[9,7]
firms500 = int(firms500)


min_firms500 = df.iloc[19,7]
min_firms500 = int(min_firms500)


per_min_firms500 = (min_firms500/firms500)*100
print(firms500)
print(min_firms500)
print(per_min_firms500)

sys.exit()




