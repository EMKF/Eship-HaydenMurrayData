import pandas as pd
import sys
import time
import matplotlib.pyplot as plt
import requests
import numpy as np
import seaborn as sns
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# time
start = time.time()

# state_codes dict, reverse dict, and recode fips to strings
state_codes = {
    'WA': 53, 'DE': 10, 'DC': 11, 'WI': 55, 'WV': 54, 'HI': 15,
    'FL': 12, 'WY': 56, 'PR': 72, 'NJ': 34, 'NM': 35, 'TX': 48,
    'LA': 22, 'NC': 37, 'ND': 38, 'NE': 31, 'TN': 47, 'NY': 36,
    'PA': 42, 'AK': 2, 'NV': 32, 'NH': 33, 'VA': 51, 'CO': 8,
    'CA': 6, 'AL': 1, 'AR': 5, 'VT': 50, 'IL': 17, 'GA': 13,
    'IN': 18, 'IA': 19, 'MA': 25, 'AZ': 4, 'ID': 16, 'CT': 9,
    'ME': 23, 'MD': 24, 'OK': 40, 'OH': 39, 'UT': 49, 'MO': 29,
    'MN': 27, 'MI': 26, 'RI': 44, 'KS': 20, 'MT': 30, 'MS': 28,
    'SC': 45, 'KY': 21, 'OR': 41, 'SD': 46
}

# pull MDJ indicators
df = pd.read_csv('s3://emkf.data.research/indicators/nej/state_nej_2020.06.24.csv')

# recode to state strings
inv_state_codes = {v: k for k, v in state_codes.items()}
df['fips'].replace(inv_state_codes, inplace=True)

# create and export long df for states
state_long_cont = df.pivot_table(index=['fips', 'firmage'], columns='time', values='contribution').reset_index()
state_long_cont.to_excel('/Users/hmurray/Desktop/data/QWI/state_long_cont.xlsx', index=False)
state_long_create = df.pivot_table(index=['fips', 'firmage'], columns='time', values='creation').reset_index()
state_long_create.to_excel('/Users/hmurray/Desktop/data/QWI/state_long_create.xlsx', index=False)

# subset for creation and contribution analysis
df = df[['fips', 'firmage', 'time', 'contribution', 'creation']]

# quality check
print(df.query('time == 2017').query('firmage == 1').sort_values(by=['contribution'], ascending=False).head())
print(df.query('fips == "CA"').query('firmage == 1').sort_values(by=['contribution'], ascending=False))
print(df.query('time == 2017').query('firmage == 1').sort_values(by=['creation'], ascending=False))
print(df.query('fips == "DC"').query('firmage == 1').sort_values(by=['creation'], ascending=False))



end = time.time()
print((end/60) - (start/60))
sys.exit()


