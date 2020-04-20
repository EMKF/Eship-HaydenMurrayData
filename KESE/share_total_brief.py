# data obtained manually from Rob Fairlie on 3.27.20 @ 12:29pm

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# # define directory
# kese_download = '/Users/hmurray/Desktop/KESE/KESE_2019_Update/2019_data_download/kese_2019_download.csv'
#
# # pull national data
# kese = pd.read_csv(kese_download)
#
# # convert to percent, as necessary
# kese['rne'] = kese['rne']*100
# kese['ose'] = kese['ose']*100
# kese['ssr'] = kese['ssr']*100
#
# # Rename columns
# kese.rename(columns={"name": "STATE", "rne": "RATE OF NEW ENTREPRENEURS", "ose": "OPPORTUNITY SHARE OF NEW ENTREPRENEURS"\
#     ,"sjc": "STARTUP EARL JOB CREATION", "ssr": "STARTUP EARLY SURVIVAL RATE", "zindex": "KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX"},inplace=True)
#
# # Figure 4, 6, 8 calculated from US -n values

# define directory
df = '/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/kese_change_share_demo.xlsx'
df = pd.read_excel(df, sheet_name='rne')
df = df[df.columns[pd.Series(df.columns).str.startswith(('demo', 'n'))]]
df = df[(df['demographic'] =='White') | (df['demographic'] =='Black') | (df['demographic'] =='Asian') |\
             (df['demographic'] =='Latino') | (df['demographic'] =='Total')].reset_index(drop=True)
df = df.set_index('demographic').transpose()
print(df)
sys.exit()



# fig_4

fig_4 = fig_4[['demographic', 'n_1996', 'n_2019']]
fig_4.set_index('demographic', inplace=True)
fig_4 = fig_4.transpose().reset_index(drop=True)
columns = list(fig_4.columns.values)
for column_1 in columns:
    for column_2 in columns:
        new_column = '-'.join([column_1,column_2])
        fig_4[new_column] = fig_4[column_1] / fig_4[column_2]
fig_4 = fig_4[['White-Total', 'Black-Total', 'Latino-Total', 'Asian-Total']]
fig_4 = fig_4.transpose().reset_index(drop=False)
fig_4.rename(columns={0: "1996", 1: "2019"},inplace=True)
fig_4['demographic'] = fig_4['demographic'].str.replace("-Total","")
print(fig_4)
fig_4.to_excel('/Users/hmurray/Desktop/data/KESE/share_total/share_race_change.xlsx', index=False)




