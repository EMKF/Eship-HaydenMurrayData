import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# add options to the end of location to avoid using too much memory
df = pd.read_csv('/Users/hmurray/Downloads/public2018.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# look at df
print(df.head())

# print frequencies
print(df['D3A'].value_counts())
print(df['D3B'].value_counts())
print(df['ppreg4'].value_counts())
print(df['ppstaten'].value_counts())

# group types of work by ...
# state_pop = df['D3B'].groupby([df['ppreg4'], df['D3B']]).count()
# print(state_pop)

# crosstab business ownership by region
print(pd.crosstab(df['ppreg4'], df['D3A']))

# crosstab work status by region
print(pd.crosstab(df['ppreg4'], df['D3B']))

# crosstab work status by state
print(pd.crosstab(df['ppstaten'], df['D3B']))

# crosstab work status by state
print(pd.crosstab(df['ppstaten'], df['D3B']))

#crosstab business ownership by work status
print(pd.crosstab(df['D3A'], df['D3B']))
