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
pd.options.mode.chained_assignment = None


# DRAFT 2 (MULTIPLE SCRIPTS IN THIS .py FILE)


# pull,
df_agg = pd.read_csv('/Users/hmurray/Desktop/data/SHED/2018_SHED_data.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# subset by business ownership and EF-
df1 = df_agg['D3A']
df2 = df_agg[df_agg.columns[pd.Series(df_agg.columns).str.startswith('EF')]]
df = pd.concat([df1, df2], axis=1)
print(df.head())

# replace "Refused" with NaN
df_agg.replace('Refused', np.nan, inplace=True)
df_agg.replace('Other (Please specify):', np.nan, inplace=True)

# shorten strings
df_agg['D3A'] = df_agg['D3A'].str.replace("For a single company or employer", "Single_Company/Employer", case = True)
df_agg['D3A'] = df_agg['D3A'].str.replace("For yourself or your family business", "Yourself/Family_Business", case = True)

# crosstab function
def crosstab_all(dataset, attributelist):
    for v in var:
        print()
        name = pd.crosstab(dataset[v],dataset["D3A"], normalize=True, margins=False)
        name.append(name)
        print(name)

var = df_agg[df_agg.columns[pd.Series(df_agg.columns).str.startswith('EF')]]
crosstab_all(df_agg, var)
