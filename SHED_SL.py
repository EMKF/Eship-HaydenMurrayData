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

# add options to the end of location to avoid using too much memory
df_agg = pd.read_csv('/Users/hmurray/Downloads/public2018.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# aggregate dataframe of 3 analyses below
df = df_agg[['SL4','ppagecat','ppinccat6', 'D3A',]]

# Convert rows of student loans with NaN to 'None' since NaN represents people with no student loan debt
df['SL4'] = df['SL4'].astype(object).replace(np.nan, 'No student loan debt')
print(df.head())

# arrange student loan categories
SL4_ordering = ["No student loan debt","$1 to $49","$50 to $99","$100 to $199","$200 to $299","$300 to $399","$400 to $499","$500 to $749","$750 to $999","$1,000 or above","I am currently not required to make any payments on these loans","Refused","Don't know"]
df["SL4"] = pd.Categorical(df.loc[:,"SL4"], categories=SL4_ordering)

# arrange income categories
inc_ordering = ["<$25,000","$25-49,999","$50-74,999","$75-99,999","$100-149,999","$150,000+"]
df["ppinccat6"] = pd.Categorical(df["ppinccat6"], categories=inc_ordering)

# debt * age
ct_sl_age = (pd.crosstab(df['SL4'], df['ppagecat'], normalize='columns'))\
    .round(4)*100
ct_sl_age.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_age.csv')
print(ct_sl_age)

# debt * income
ct_sl_inc = (pd.crosstab(df['SL4'], df['ppinccat6'], normalize='columns'))\
    .round(4)*100
ct_sl_inc.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_inc.csv')
print(ct_sl_inc)

# debt * eship or ownership
ct_sl_eship = (pd.crosstab(df['SL4'], df['D3A'], normalize='columns'))\
    .round(4)*100
ct_sl_eship.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_eship.csv')
print(ct_sl_eship)

# plots
