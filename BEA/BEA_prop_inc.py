import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# pull BEA employment data
emp = pd.read_csv('/Users/hmurray/Desktop/data/BEA/BEA_Data/BEA_employment.csv')

# pull BEA income data
inc = pd.read_csv('/Users/hmurray/Desktop/data/BEA/BEA_Data/BEA_income.csv')

# subset using startswith()
emp = emp[emp.columns[pd.Series(emp.columns).str.startswith(('GeoName', 'Description', '2'))]]
inc = inc[inc.columns[pd.Series(inc.columns).str.startswith(('GeoName', 'Description', '2'))]]

# convert to numeric
df_inc['2018:Q1'] = pd.to_numeric(df_inc['2018:Q1'])

# sum quarterly values of income
# inc['2018'] = inc['2018:Q1'] + inc['2018:Q2'] + inc['2018:Q3'] + inc['2018:Q4']
inc.groupby((np.arange(len(inc.columns)) // 4) + 1, axis=1).sum().add_prefix('s')

print(emp.head(100))
print(inc.head(100))
sys.exit()

# FILTER FUNCTION
def filterer(df):
    df = df[df['region'] == 'United States']
    df = df[df['industry'] == 'Total for all sectors']
    df = df[(df.demographic == 'All firms') | (df.demographic == 'Male')\
            | (df.demographic == 'Female') | (df.demographic == 'Hispanic') | (df.demographic == 'White')\
            | (df.demographic == 'Asian') | (df.demographic == 'Black or African American')]
    df = df[(df.firm_age == 'All firms') | (df.firm_age == 'Firms with less than 2 years in business')]
    df.reset_index(inplace=True, drop=True)
    df.drop(df.columns[0:2], axis=1, inplace=True)
    df.reset_index(inplace=True, drop=True)
    return df
reasons = filterer(reasons)

# merge dataframes
df_merge = pd.merge(df_emp, df_inc, on='GeoName')
print(df_merge)
