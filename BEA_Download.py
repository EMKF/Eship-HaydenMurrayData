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

df1 = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/BEA/BEA_Data/BEA_employment.csv')
df_emp = df1[['GeoName','Description','2018']]
print(df_emp.head())

df2 = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/BEA/BEA_Data/BEA_income.csv')
df_inc = df2[['GeoName','Description','2018:Q1','2018:Q2','2018:Q3','2018:Q4']]
print(df_inc.head())

# df3 = df2['GeoName'], (df2['2018:Q1']+df2['2018:Q2']), True
# print(df3)

