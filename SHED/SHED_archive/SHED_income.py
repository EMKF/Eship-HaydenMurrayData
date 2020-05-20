import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
import xlsxwriter

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None


# pull,
df_agg = pd.read_csv('/Users/hmurray/Desktop/data/SHED/2018_SHED_data.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# replace "Refused" with NaN
df_agg.replace('Refused', np.nan, inplace=True)
df_agg.replace('Other (Please specify):', np.nan, inplace=True)

# shorten strings
df_agg['D3A'] = df_agg['D3A'].str.replace("For a single company or employer", "Employed", case = True)
df_agg['D3A'] = df_agg['D3A'].str.replace("For yourself or your family business", "Family- or Self-Employed", case = True)

# subset
df = df_agg[df_agg.columns[pd.Series(df_agg.columns).str.startswith(('D3A', 'I4', 'I12'))]]
print(df.head())

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/inc_crosstabs.xlsx', engine='xlsxwriter')

def crosser(attributelist):
    for k in attributelist:
        xtab = pd.crosstab(df[k], df['D3A'], normalize='columns').round(4)*100
        print(xtab)
        print('')
        # export crosstabs to excel sheets
        xtab.to_excel(writer, sheet_name=str(k), index=True)



attributelist = list(df.columns)
print(attributelist)
crosser(attributelist)
writer.save()

sys.exit()
