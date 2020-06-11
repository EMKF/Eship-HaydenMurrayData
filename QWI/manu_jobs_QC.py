# data obtained manually from https://ledextract.ces.census.gov/static/data.html
# unemployment rate from BLS series number LNS14000000: https://data.bls.gov/timeseries/LNS14000000

import pandas as pd
import os
import sys
import requests
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# contribution
# EMP(year, region, all age categories) / EMP(year, region, specific age categories)
# US, state, AL counties, OK counties, UT counties,
contribution = pd.DataFrame()
for csv in os.listdir('/Users/hmurray/Desktop/Jobs_Indicators/data_check/contribution/'):
    print(csv)
    df = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/data_check/contribution/' + str(csv))
    contribution = contribution.append(df, sort=True)

contribution = contribution[['geography', 'year', 'quarter', 'firmage', 'Emp']]
contribution = contribution.groupby(['geography', 'year', 'firmage']).agg({'Emp': 'sum'}).reset_index()
total_contribution = contribution.groupby(['geography', 'year']).agg({'Emp': 'sum'}).reset_index()
df = contribution.merge(total_contribution, on=['geography', 'year'])
df.rename(columns={'geography': 'fips', 'Emp_x':'age_emp', 'Emp_y': 'total_emp'}, inplace=True)
df['contribution'] = (df['age_emp'] / df['total_emp']) * 100
print(df)

# check
