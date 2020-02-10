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
df_agg = pd.read_csv('/Users/hmurray/Downloads/public2018.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# aggregate dataframe of 3 analyses below
df = df_agg[['SL4','ppagecat','ppinccat6', 'D3A',]]
print(df.head())

# drop rows with missing values (NaN)
# df= df.dropna()

# reset index
df.reset_index(inplace=True, drop=True)

# sort columns by category size
# df['SL4'] = df['SL4'].\
#     map().\
#     pipe(pd.Categorical, categories=['$1 to $49', '$50 to $99', '$100 to $199', '$200 to $299', '$300 to $399', '$400 to $499', '$500 to $749', '$750 to $999', '$1,000 or above'], ordered=True)

# debt * age
ct_sl_age = (pd.crosstab(df['SL4'], df['ppagecat']))
ct_sl_age.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_age.csv')
print(ct_sl_age)

# debt * income
ct_sl_inc = (pd.crosstab(df['SL4'], df['ppinccat6']))
ct_sl_inc.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_inc.csv')
print(ct_sl_inc)

# debt * eship or ownership
ct_sl_eship = (pd.crosstab(df['SL4'], df['D3A']))
ct_sl_eship.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_eship.csv')
print(ct_sl_eship)