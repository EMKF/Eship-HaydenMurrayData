# data obtained manually from Rob Fairlie on 3.27.20 @ 12:29pm

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap
from matplotlib.ticker import FormatStrFormatter

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# define directory
kese_download = '/Users/hmurray/Desktop/KESE/KESE_2019_Update/2019_data_download/kese_download_2020.07.23.csv'

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

# remove USA
med = kese[(kese['STATE'] != 'United States')].reset_index(drop=True)

# median calculation prep
med_rne = med[['STATE', 'year', 'RATE OF NEW ENTREPRENEURS']]
med_ose = med[['STATE', 'year', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
med_sjc = med[['STATE', 'year', 'STARTUP EARLY JOB CREATION']]
med_sesr = med[['STATE', 'year', 'STARTUP EARLY SURVIVAL RATE']]
med_index = med[['STATE', 'year', 'KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX']]

def pivoter(df, indicator):
    df = df.groupby('year').agg({indicator: np.median}).reset_index()
    df.dropna(inplace=True)
    print(df.head())
    print(df.columns)
    return df

med_rne = pivoter(med_rne, 'RATE OF NEW ENTREPRENEURS')
med_ose = pivoter(med_ose, 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS')
med_sjc = pivoter(med_sjc, 'STARTUP EARLY JOB CREATION')
med_sesr = pivoter(med_sesr, 'STARTUP EARLY SURVIVAL RATE')
med_index = pivoter(med_index, 'KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX')


#############################################################################################################################
############################################# RATE OF NEW ENTREPRENEURS #####################################################
#############################################################################################################################

# rne_max_min_med
rne_max_min_med = kese[(kese['type'] =='Total') & (kese['STATE']=='Rhode Island') | (kese['STATE']=='Florida')].reset_index(drop=True)
rne_max_min_med = rne_max_min_med[['STATE', 'year', 'RATE OF NEW ENTREPRENEURS']]
print(rne_max_min_med)
rne_max_min_med = rne_max_min_med.pivot_table(index=['year'], columns='STATE', values='RATE OF NEW ENTREPRENEURS').reset_index()
print(rne_max_min_med)

rne_plot = rne_max_min_med.merge(med_rne, on='year')
rne_plot.rename(columns={"RATE OF NEW ENTREPRENEURS": "Yearly Median"},inplace=True)
rne_plot['year'] = rne_plot['year'].astype(str)
print(rne_plot)
sys.exit()
rne_plot.plot(x='year', y=['Rhode Island', 'Florida', 'Yearly Median'])
plt.title("\n".join(wrap("FIGURE 19 RATE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST AND HIGHEST IN 2019 AND YEARLY MEDIAN)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.5])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/rne2.png')
plt.show()


#############################################################################################################################
######################################## OPPORTUNITY SHARE OF NEW ENTREPRENEURS #############################################
#############################################################################################################################


# Figure 18
ose_max_min_med = kese[(kese['type'] =='Total') & (kese['STATE']=='South Dakota') | (kese['STATE']=='District of Columbia')].reset_index(drop=True)
ose_max_min_med = ose_max_min_med[['STATE', 'year', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
ose_max_min_med = ose_max_min_med.pivot_table(index=['year'], columns='STATE', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
ose_plot = ose_max_min_med.merge(med_ose, on='year')
ose_plot.rename(columns={"OPPORTUNITY SHARE OF NEW ENTREPRENEURS": "Yearly Median"},inplace=True)
ose_plot['year'] = ose_plot['year'].astype(str)
ose_plot.plot(x='year', y=['South Dakota', 'District of Columbia', 'Yearly Median'])
plt.title("\n".join(wrap("FIGURE 21 OPPORTUNITY SHARE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST AND HIGHEST IN 2019 AND YEARLY MEDIAN)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/ose2.png')
plt.show()



#############################################################################################################################
################################################ STARTUP EARLY JOB CREATION #################################################
#############################################################################################################################

# Figure 21
sjc_max_min_med = kese[(kese['type'] =='Total') & (kese['STATE']=='South Dakota') | (kese['STATE']=='District of Columbia')].reset_index(drop=True)
sjc_max_min_med = sjc_max_min_med[['STATE', 'year', 'STARTUP EARLY JOB CREATION']]
sjc_max_min_med = sjc_max_min_med.pivot_table(index=['year'], columns='STATE', values='STARTUP EARLY JOB CREATION').reset_index()
sjc_plot = sjc_max_min_med.merge(med_sjc, on='year')
sjc_plot.rename(columns={"STARTUP EARLY JOB CREATION": "Yearly Median"},inplace=True)
sjc_plot['year'] = sjc_plot['year'].astype(str)
sjc_plot.plot(x='year', y=['South Dakota', 'District of Columbia', 'Yearly Median'])
plt.title("\n".join(wrap("FIGURE 23 STARTUP EARLY JOB CREATION OVER TIME (1998–2019) (LOWEST AND HIGHEST IN 2019 AND YEARLY MEDIAN)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,25])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/sjc2.png')
plt.show()


#############################################################################################################################
################################################ STARTUP EARLY SURVIVAL RATE ################################################
#############################################################################################################################


# Figure 24
sesr_max_min_med = kese[(kese['type'] =='Total') & (kese['STATE']=='Connecticut') | (kese['STATE']=='Virginia')].reset_index(drop=True)
sesr_max_min_med = sesr_max_min_med[['STATE', 'year', 'STARTUP EARLY SURVIVAL RATE']]
sesr_max_min_med = sesr_max_min_med.pivot_table(index=['year'], columns='STATE', values='STARTUP EARLY SURVIVAL RATE').reset_index()
sesr_plot = sesr_max_min_med.merge(med_sesr, on='year')
sesr_plot.rename(columns={"STARTUP EARLY SURVIVAL RATE": "Yearly Median"},inplace=True)
sesr_plot['year'] = sesr_plot['year'].astype(str)
sesr_plot.plot(x='year', y=['Connecticut', 'Virginia', 'Yearly Median'])
plt.title("\n".join(wrap("FIGURE 25 STARTUP EARLY SURVIVAL RATE OVER TIME (1998–2019) (LOWEST AND HIGHEST IN 2019 AND YEARLY MEDIAN)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/sesr2.png')
plt.show()


#############################################################################################################################
######################################################## KESE INDEX #########################################################
#############################################################################################################################


# Figure 27
index_max_min_med = kese[(kese['type'] =='Total') & (kese['STATE']=='California') | (kese['STATE']=='Connecticut')].reset_index(drop=True)
index_max_min_med = index_max_min_med[['STATE', 'year', 'KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX']]
index_max_min_med = index_max_min_med.pivot_table(index=['year'], columns='STATE', values='KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX').reset_index()
index_plot = index_max_min_med.merge(med_index, on='year')
index_plot.rename(columns={"KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX": "Yearly Median"},inplace=True)
index_plot['year'] = index_plot['year'].astype(str)
index_plot.plot(x='year', y=['California', 'Connecticut', 'Yearly Median'])
plt.title("\n".join(wrap("FIGURE 27 KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX OVER TIME (1998–2019) (LOWEST AND HIGHEST IN 2019 AND YEARLY MEDIAN)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([-10,10])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/index2.png')
plt.show()


# #############################################################################################################################
# ############################################# RATE OF NEW ENTREPRENEURS #####################################################
# #############################################################################################################################
#
# # Figure 9
# fig_9 = kese[(kese['type'] =='Total') & (kese['STATE']=='Rhode Island') | (kese['STATE']=='Florida') | (kese['STATE']=='New York')].reset_index(drop=True)
# fig_9 = fig_9[['STATE', 'year', 'RATE OF NEW ENTREPRENEURS']]
#
# fig_9 = fig_9.pivot_table(index=['year'], columns='STATE', values='RATE OF NEW ENTREPRENEURS').reset_index()
# fig_9.plot(x='year', y=['Rhode Island', 'Florida', 'New York'])
# plt.title("\n".join(wrap("FIGURE 19 RATE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
# axes = plt.gca()
# plt.tight_layout()
# axes.set_ylim([0,.5])
# plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/rne2.png')
#
#
#
# #############################################################################################################################
# ######################################## OPPORTUNITY SHARE OF NEW ENTREPRENEURS #############################################
# #############################################################################################################################
#
#
# # Figure 18
# fig_18 = kese[(kese['type'] =='Total') & (kese['STATE']=='South Dakota') | (kese['STATE']=='District of Columbia') | (kese['STATE']=='Maryland')].reset_index(drop=True)
# fig_18 = fig_18[['STATE', 'year', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
# fig_18 = fig_18.pivot_table(index=['year'], columns='STATE', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
# fig_18.plot(x='year', y=['South Dakota', 'District of Columbia', 'Maryland'])
# plt.title("\n".join(wrap("FIGURE 21 OPPORTUNITY SHARE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
# axes = plt.gca()
# plt.tight_layout()
# axes.set_ylim([50,100])
# plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/ose2.png')
#
#
#
# #############################################################################################################################
# ################################################ STARTUP EARLY JOB CREATION #################################################
# #############################################################################################################################
#
# # Figure 21
# fig_21 = kese[(kese['type'] =='Total') & (kese['STATE']=='South Dakota') | (kese['STATE']=='District of Columbia') | (kese['STATE']=='Alabama')].reset_index(drop=True)
# fig_21 = fig_21[['STATE', 'year', 'STARTUP EARLY JOB CREATION']]
# fig_21 = fig_21.pivot_table(index=['year'], columns='STATE', values='STARTUP EARLY JOB CREATION').reset_index()
# fig_21.plot(x='year', y=['South Dakota', 'District of Columbia', 'Alabama'])
# plt.title("\n".join(wrap("FIGURE 23 STARTUP EARLY JOB CREATION OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
# axes = plt.gca()
# plt.tight_layout()
# axes.set_ylim([0,25])
# plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/sjc2.png')
#
# #############################################################################################################################
# ################################################ STARTUP EARLY SURVIVAL RATE ################################################
# #############################################################################################################################
#
#
# # Figure 24
# fig_24 = kese[(kese['type'] =='Total') & (kese['STATE']=='Connecticut') | (kese['STATE']=='Virginia') | (kese['STATE']=='Tennessee')].reset_index(drop=True)
# fig_24 = fig_24[['STATE', 'year', 'STARTUP EARLY SURVIVAL RATE']]
# fig_24 = fig_24.pivot_table(index=['year'], columns='STATE', values='STARTUP EARLY SURVIVAL RATE').reset_index()
# fig_24.plot(x='year', y=['Connecticut', 'Virginia', 'Tennessee'])
# plt.title("\n".join(wrap("FIGURE 25 STARTUP EARLY SURVIVAL RATE OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
# axes = plt.gca()
# plt.tight_layout()
# axes.set_ylim([50,100])
# plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/sesr2.png')
#
#
#
# #############################################################################################################################
# ######################################################## KESE INDEX #########################################################
# #############################################################################################################################
#
#
# # Figure 27
# fig_27 = kese[(kese['type'] =='Total') & (kese['STATE']=='California') | (kese['STATE']=='Connecticut') | (kese['STATE']=='Nebraska')].reset_index(drop=True)
# fig_27 = fig_27[['STATE', 'year', 'KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX']]
# fig_27 = fig_27.pivot_table(index=['year'], columns='STATE', values='KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX').reset_index()
# fig_27['year'] = pd.to_datetime(fig_27['year'], format='%Y')
# fig_27.plot(x='year', y=['California', 'Connecticut', 'Nebraska'])
# plt.title("\n".join(wrap("FIGURE 27 KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
# axes = plt.gca()
# plt.tight_layout()
# axes.set_ylim([-10,10])
# plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/index2.png')
#
# plt.show()