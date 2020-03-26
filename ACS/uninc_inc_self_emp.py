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


# pull,
df_all = pd.read_csv('/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/median_earnings_2005_2018_gender.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)
print(df_all)
# rename strings
df_all['employment_type'] = df_all['employment_type'].str.replace("private_self_employed", "inc_self", case = True)
df_all['employment_type'] = df_all['employment_type'].str.replace("self_employed_not_inc", "uninc_self", case = True)

# filter
df_overall = df_all[(df_all.employment_type == 'inc_self') | (df_all.employment_type == 'uninc_self') | (df_all.employment_type == 'total')]
df_overall = df_overall[(df_overall.gender == 'overall')]
print(df_overall)

df_gender = df_all[(df_all.employment_type == 'inc_self') | (df_all.employment_type == 'uninc_self') | (df_all.employment_type == 'total')]
# df_gender = df_gender[(df_overall.gender == 'overall')]
print(df_gender)

# unstack
df_overall = df_overall.pivot(index='employment_type', columns='year', values='median_earnings')
print (df_overall)
df_overall.to_excel('/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/total_in_un.xlsx', index=False)

# df_gender = df_gender.pivot(index=('employment_type', 'gender'), columns='year', values='median_earnings')
df_gender = (df_gender.pivot_table(index=['employment_type','gender'],columns='year', values='median_earnings')
       .reset_index()
       .rename_axis(None, axis=1))
print(df_gender)
df_gender.to_excel('/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/gender_in_un.xlsx', index=False)

sys.exit()