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

# define directory
kese_download = '/Users/hmurray/Desktop/KESE/KESE_2019_Update/2019_data_download/kese_2019_download.csv'

# pull national data
kese = pd.read_csv(kese_download)

# convert to percent, as necessary
kese['rne'] = kese['rne']*100
kese['ose'] = kese['ose']*100
kese['ssr'] = kese['ssr']*100

# Rename columns
kese.rename(columns={"name": "STATE", "rne": "RATE OF NEW ENTREPRENEURS", "ose": "OPPORTUNITY SHARE OF NEW ENTREPRENEURS"\
    ,"sjc": "STARTUP EARL JOB CREATION", "ssr": "STARTUP EARLY SURVIVAL RATE", "zindex": "KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX"},inplace=True)

# Table 1
tab_1 = kese[(kese['category']=='Total') & (kese['year']==2019)].reset_index(drop=True)
tab_1.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_1.xlsx', index=False)



#############################################################################################################################
############################################# RATE OF NEW ENTREPRENEURS #####################################################
#############################################################################################################################



# Figure 1
fig_1 = kese[(kese['STATE'] =='United States') & (kese['type']=='Total')].reset_index(drop=True)
fig_1 = fig_1[['STATE', 'year', 'RATE OF NEW ENTREPRENEURS']]
fig_1.plot(x='year', y=['RATE OF NEW ENTREPRENEURS'])
plt.title("\n".join(wrap("FIGURE 1 RATE OF NEW ENTREPRENEURS OVER TIME (1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.5])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_1.png')

# Table 2
tab_2 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
tab_2 = kese[(kese['category'] =='Female') | (kese['category'] =='Male') | (kese['category'] =='Total')].reset_index(drop=True)
tab_2 = tab_2[['STATE', 'year', 'category', 'RATE OF NEW ENTREPRENEURS']]
tab_2 = tab_2.pivot_table(index=['year'], columns='category', values='RATE OF NEW ENTREPRENEURS').reset_index()
tab_2.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_2.xlsx', index=False)

# Figure 2
tab_2.plot(x='year', y=['Female', 'Male'])
plt.title("\n".join(wrap("FIGURE 2 RATE OF NEW ENTREPRENEURS BY SEX (1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.5])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_2.png')

# Table 3
tab_3 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
tab_3 = kese[(kese['category'] =='White') | (kese['category'] =='Black') | (kese['category'] =='Asian') |\
             (kese['category'] =='Latino') | (kese['category'] =='Total')].reset_index(drop=True)
tab_3 = tab_3[['STATE', 'year', 'category', 'RATE OF NEW ENTREPRENEURS']]
tab_3 = tab_3.pivot_table(index=['year'], columns='category', values='RATE OF NEW ENTREPRENEURS').reset_index()
tab_3.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_3.xlsx', index=False)

# Figure 3
tab_3.plot(x='year', y=['White', 'Asian', 'Black', 'Latino'])
plt.title("\n".join(wrap("FIGURE 3 RATE OF NEW ENTREPRENEURS BY RACE AND ETHNICITY (1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.6])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_3.png')

# Table 4
tab_4 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
tab_4 = kese[(kese['category'] =='Native-Born') | (kese['category'] =='Immigrant') | (kese['category'] =='Total')].reset_index(drop=True)
tab_4 = tab_4[['STATE', 'year', 'category', 'RATE OF NEW ENTREPRENEURS']]
tab_4 = tab_4.pivot_table(index=['year'], columns='category', values='RATE OF NEW ENTREPRENEURS').reset_index()
tab_4.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_4.xlsx', index=False)

# Figure 4
tab_4.plot(x='year', y=['Immigrant', 'Native-Born'])
plt.title("\n".join(wrap("FIGURE 4 RATE OF NEW ENTREPRENEURS BY NATIVITY(1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.7])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_4.png')

# Table 5
tab_5 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
tab_5 = kese[(kese['category'] =='Ages 20-34') | (kese['category'] =='Ages 35-44') | (kese['category'] =='Ages 45-54') |\
             (kese['category'] =='Ages 55-64') | (kese['category'] =='Total')].reset_index(drop=True)
tab_5 = tab_5[['STATE', 'year', 'category', 'RATE OF NEW ENTREPRENEURS']]
tab_5 = tab_5.pivot_table(index=['year'], columns='category', values='RATE OF NEW ENTREPRENEURS').reset_index()
tab_5.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_5.xlsx', index=False)

# Figure 5
tab_5.plot(x='year', y=['Ages 20-34', 'Ages 35-44', 'Ages 45-54', 'Ages 55-64'])
plt.title("\n".join(wrap("FIGURE 5 RATE OF NEW ENTREPRENEURS BY AGE (1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.7])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_5.png')

# Table 6
tab_6 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
tab_6 = kese[(kese['category'] =='Less than High School') | (kese['category'] =='High School Graduate') | (kese['category'] =='Some College') |\
             (kese['category'] =='College Graduate') | (kese['category'] =='Total')].reset_index(drop=True)
tab_6 = tab_6[['STATE', 'year', 'category', 'RATE OF NEW ENTREPRENEURS']]
tab_6 = tab_6.pivot_table(index=['year'], columns='category', values='RATE OF NEW ENTREPRENEURS').reset_index()
tab_6.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_6.xlsx', index=False)

# Figure 6
tab_6.plot(x='year', y=['Less than High School', 'High School Graduate', 'Some College', 'College Graduate'])
plt.title("\n".join(wrap("FIGURE 6 RATE OF NEW ENTREPRENEURS BY EDUCATION (1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.7])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_6.png')

# Table 7
tab_7 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
tab_7 = kese[(kese['category'] =='Veterans') | (kese['category'] =='Non-Veterans') | (kese['category'] =='Total')].reset_index(drop=True)
tab_7 = tab_7[['STATE', 'year', 'category', 'RATE OF NEW ENTREPRENEURS']]
tab_7 = tab_7.pivot_table(index=['year'], columns='category', values='RATE OF NEW ENTREPRENEURS').reset_index()
tab_7.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_7.xlsx', index=False)

# Figure 7
tab_7.plot(x='year', y=['Non-Veterans', 'Veterans'])
plt.title("\n".join(wrap("FIGURE 7 RATE OF NEW ENTREPRENEURS BY VETERAN STATUS (1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.7])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_7.png')

# Figure 8
fig_8 = kese[(kese['type'] =='Total') & (kese['year']==2019)].reset_index(drop=True)
fig_8 = fig_8[['STATE', 'RATE OF NEW ENTREPRENEURS']]
fig_8.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_8.xlsx', index=False)

# Figure 9
fig_9 = kese[(kese['type'] =='Total') & (kese['STATE']=='Rhode Island') | (kese['STATE']=='Florida') | (kese['STATE']=='New York')].reset_index(drop=True)
fig_9 = fig_9[['STATE', 'year', 'RATE OF NEW ENTREPRENEURS']]
fig_9['STATE'] = fig_9['STATE'].str.replace("New York", "Median", case = True)
fig_9 = fig_9.pivot_table(index=['year'], columns='STATE', values='RATE OF NEW ENTREPRENEURS').reset_index()
print()
print(fig_9.agg)
fig_9.plot(x='year', y=['Rhode Island', 'Florida', 'Median'])
plt.title("\n".join(wrap("FIGURE 9 RATE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.5])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_9.png')



#############################################################################################################################
######################################## OPPORTUNITY SHARE OF NEW ENTREPRENEURS #############################################
#############################################################################################################################



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
