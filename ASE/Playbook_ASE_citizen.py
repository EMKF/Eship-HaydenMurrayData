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
df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_citizenship/ASE_2016_00CSCBO09_with_ann.csv')

# keep vars
df = df[['GEO.display-label', 'NAICS.display-label', 'ASECBO.display-label', 'YIBSZFI.display-label', 'USBORNCIT.display-label','OWNPDEMP', 'OWNPDEMP_PCT']]

# Rename columns
df.rename(columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECBO.display-label": "demographic"\
    ,"YIBSZFI.display-label": "firm_age", "USBORNCIT.display-label": "citizen", "OWNPDEMP_PCT": "percent"},inplace=True)

# filters
df = df[df['region'] == 'United States']
df = df[df['industry'] == 'Total for all sectors']
df = df[df['firm_age'] == 'All firms']

# filter for minority, white, and total
df = df[(df.demographic == 'All owners of respondent firms') | (df.demographic == 'White') | (df.demographic == 'Minority') | (df.demographic == 'Nonminority')]

# reset index
df.reset_index(inplace=True, drop=True)
print(df)

# total firms
total_firms = df.iloc[2,5]
total_firms = int(total_firms)
print(total_firms)

# white firms
white_firms = df.iloc[6,5]
white_firms = int(white_firms)
print(white_firms)

# minority firms
min_firms = df.iloc[10,5]
min_firms = int(min_firms)
print(int(min_firms))

# Nonminority firms
nonmin_firms = df.iloc[14,5]
nonmin_firms = int(nonmin_firms)
print(int(nonmin_firms))

# percent white firms
white_firms_per = (white_firms/total_firms)*100
print(white_firms_per)

# percent minority firms
min_firms_per = (min_firms/total_firms)*100
print(min_firms_per)

# percent Nonminority firms
nonmin_firms_per = (nonmin_firms/total_firms)*100
print(nonmin_firms_per)

