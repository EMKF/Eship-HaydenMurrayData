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


# aggregate dataframe of 3 analyses below
# df_agg = df[['ppage','ppagecat','D3A','D3B','ppreg4','ppstaten','SL3','SL4','FS20_b']]
# print(df_agg.head())

# create student loan data frames
sl_age = df[['SL3','SL4','FS20_b','ppage','ppagecat']]
sl_inc = df[['SL3','SL4','FS20_b','ppincimp','ppinccat6']]
sl_eship = df[['SL3','SL4','FS20_b','D3A']]


# drop rows with missing values (NaN)
# sl_age = sl_age.dropna()
# sl_inc = sl_inc.dropna()
# sl_eship = sl_eship.dropna()

# reset index
sl_age.reset_index(inplace=True, drop=True)
sl_inc.reset_index(inplace=True, drop=True)
sl_eship.reset_index(inplace=True, drop=True)

# sort columns by category size
# sl_age.sort_values(by=['ppagecat'],ascending = True, inplace = True)
# sl_inc.sort_values(by=['ppinccat6'],ascending = True, inplace = True)
# sl_eship.sort_values(by=['SL4'],ascending = True, inplace = True)

# debt * age
ct_sl_age = (pd.crosstab(sl_age['SL4'], sl_age['ppagecat']))
ct_sl_age.to_csv('/Users/Hmurray/Desktop/ct_sl_age.csv')
print(ct_sl_age)

# debt * income
ct_sl_inc = (pd.crosstab(sl_inc['SL4'], sl_inc['ppinccat6']))
ct_sl_inc.to_csv('/Users/Hmurray/Desktop/ct_sl_inc.csv')
print(ct_sl_inc)

# debt * eship or ownership
ct_sl_eship = (pd.crosstab(sl_eship['SL4'], sl_eship['D3A']))
ct_sl_eship.to_csv('/Users/Hmurray/Desktop/ct_sl_eship.csv')
print(ct_sl_eship)