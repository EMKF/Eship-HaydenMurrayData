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
pd.set_option('display.float_format', lambda x: '%.5f' % x)
pd.options.mode.chained_assignment = None

# define directory
kese_download = '/Users/hmurray/Desktop/KESE/KESE_2019_Update/2019_data_download/kese_2019_download.csv'

# pull national data
kese = pd.read_csv(kese_download)

# convert to percent, as necessary
kese['rne'] = kese['rne']*100
kese['ose'] = kese['ose']*100
kese['ssr'] = kese['ssr']*100
print(kese.head())

# Rename columns
kese.rename(columns={"name": "STATE", "rne": "RATE OF NEW ENTREPRENEURS", "ose": "OPPORTUNITY SHARE OF NEW ENTREPRENEURS"\
    ,"sjc": "STARTUP EARL JOB CREATION", "ssr": "STARTUP EARLY SURVIVAL RATE", "zindex": "KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX"},inplace=True)

# Table 1
tab_1 = kese[(kese['category']=='Total') & (kese['year']==2019)].reset_index(drop=True)
tab_1.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_1.xlsx', index=False)

# Figure 1
fig_1 = kese[(kese['STATE'] =='United States') & (kese['type']=='Total')].reset_index(drop=True)
fig_1 = fig_1[['STATE', 'year', 'RATE OF NEW ENTREPRENEURS']]
fig_1.plot(x='year', y=['RATE OF NEW ENTREPRENEURS'])
plt.title("\n".join(wrap("FIGURE 2 RATE OF NEW ENTREPRENEURS OVER TIME (1998–2018) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2018)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.5])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_1.png')

# Table 2
tab_2 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
tab_2 = kese[(kese['category'] =='Female') | (kese['category'] =='Male')].reset_index(drop=True)
tab_2 = tab_2[['STATE', 'year', 'category', 'RATE OF NEW ENTREPRENEURS']]
tab_2.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_2.xlsx', index=False)
print(tab_2)

# # Figure 2
# fig_1 = kese[(kese['STATE']=='United States') & (kese['type'] =='Female') | (kese['type'] =='Male')].reset_index(drop=True)
# fig_1 = fig_1[['STATE', 'year', 'RATE OF NEW ENTREPRENEURS']]
# fig_1.plot(x='year', y=['RATE OF NEW ENTREPRENEURS'])
# plt.title("\n".join(wrap("FIGURE 2 RATE OF NEW ENTREPRENEURS OVER TIME (1998–2018) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2018)", 50)))
# axes = plt.gca()
# plt.tight_layout()
# axes.set_ylim([0,.5])
# plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_1.png')
# plt.show()




# # Create a Pandas Excel writer using XlsxWriter as the engine.
# writer = pd.ExcelWriter('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_1.xlsx', engine='xlsxwriter')
#
# def crosser(list):
#     for k in list:
#         xtab = pd.crosstab(df[k], df['D3A'], normalize='columns').round(4)*100
#         print(xtab)
#         print('')
#         # export crosstabs to excel sheets
#         xtab.to_excel(writer, sheet_name=str(k), index=True)
# list = list(df.columns)
# print(list)
# crosser(list)
# writer.save()
