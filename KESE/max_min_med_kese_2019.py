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
    ,"sjc": "STARTUP EARLY JOB CREATION", "ssr": "STARTUP EARLY SURVIVAL RATE", "zindex": "KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX"},inplace=True)

# Table 1
tab_1 = kese[(kese['category']=='Total') & (kese['year']==2019)].reset_index(drop=True)
tab_1.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/table_1.xlsx', index=False)



#############################################################################################################################
############################################# RATE OF NEW ENTREPRENEURS #####################################################
#############################################################################################################################

# Figure 9
fig_9 = kese[(kese['type'] =='Total') & (kese['STATE']=='Rhode Island') | (kese['STATE']=='Florida') | (kese['STATE']=='New York')].reset_index(drop=True)
fig_9 = fig_9[['STATE', 'year', 'RATE OF NEW ENTREPRENEURS']]

fig_9 = fig_9.pivot_table(index=['year'], columns='STATE', values='RATE OF NEW ENTREPRENEURS').reset_index()
fig_9.plot(x='year', y=['Rhode Island', 'Florida', 'New York'])
plt.title("\n".join(wrap("FIGURE 19 RATE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.5])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/rne2.png')



#############################################################################################################################
######################################## OPPORTUNITY SHARE OF NEW ENTREPRENEURS #############################################
#############################################################################################################################


# Figure 18
fig_18 = kese[(kese['type'] =='Total') & (kese['STATE']=='South Dakota') | (kese['STATE']=='District of Columbia') | (kese['STATE']=='Maryland')].reset_index(drop=True)
fig_18 = fig_18[['STATE', 'year', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_18 = fig_18.pivot_table(index=['year'], columns='STATE', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
fig_18.plot(x='year', y=['South Dakota', 'District of Columbia', 'Maryland'])
plt.title("\n".join(wrap("FIGURE 21 OPPORTUNITY SHARE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/ose2.png')



#############################################################################################################################
################################################ STARTUP EARLY JOB CREATION #################################################
#############################################################################################################################

# Figure 21
fig_21 = kese[(kese['type'] =='Total') & (kese['STATE']=='South Dakota') | (kese['STATE']=='District of Columbia') | (kese['STATE']=='Alabama')].reset_index(drop=True)
fig_21 = fig_21[['STATE', 'year', 'STARTUP EARLY JOB CREATION']]
fig_21 = fig_21.pivot_table(index=['year'], columns='STATE', values='STARTUP EARLY JOB CREATION').reset_index()
fig_21.plot(x='year', y=['South Dakota', 'District of Columbia', 'Alabama'])
plt.title("\n".join(wrap("FIGURE 23 STARTUP EARLY JOB CREATION OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,25])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/sjc2.png')

#############################################################################################################################
################################################ STARTUP EARLY SURVIVAL RATE ################################################
#############################################################################################################################


# Figure 24
fig_24 = kese[(kese['type'] =='Total') & (kese['STATE']=='Connecticut') | (kese['STATE']=='Virginia') | (kese['STATE']=='Tennessee')].reset_index(drop=True)
fig_24 = fig_24[['STATE', 'year', 'STARTUP EARLY SURVIVAL RATE']]
fig_24 = fig_24.pivot_table(index=['year'], columns='STATE', values='STARTUP EARLY SURVIVAL RATE').reset_index()
fig_24.plot(x='year', y=['Connecticut', 'Virginia', 'Tennessee'])
plt.title("\n".join(wrap("FIGURE 25 STARTUP EARLY SURVIVAL RATE OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/sesr2.png')



#############################################################################################################################
######################################################## KESE INDEX #########################################################
#############################################################################################################################


# Figure 27
fig_27 = kese[(kese['type'] =='Total') & (kese['STATE']=='California') | (kese['STATE']=='Connecticut') | (kese['STATE']=='Nebraska')].reset_index(drop=True)
fig_27 = fig_27[['STATE', 'year', 'KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX']]
fig_27 = fig_27.pivot_table(index=['year'], columns='STATE', values='KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX').reset_index()
fig_27['year'] = pd.to_datetime(fig_27['year'], format='%Y')
fig_27.plot(x='year', y=['California', 'Connecticut', 'Nebraska'])
plt.title("\n".join(wrap("FIGURE 26 KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([-10,10])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/index2.png')

plt.show()