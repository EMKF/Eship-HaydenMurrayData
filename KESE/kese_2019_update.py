# data obtained manually from Rob Fairlie on 3.27.20 @ 12:29pm

import pandas as pd
import matplotlib.pyplot as plt
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
fig_9.plot(x='year', y=['Rhode Island', 'Florida', 'Median'])
plt.title("\n".join(wrap("FIGURE 19 RATE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,.5])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_9.png')



#############################################################################################################################
######################################## OPPORTUNITY SHARE OF NEW ENTREPRENEURS #############################################
#############################################################################################################################



# Figure 10
fig_10 = kese[(kese['STATE'] =='United States') & (kese['type']=='Total')].reset_index(drop=True)
fig_10 = fig_10[['STATE', 'year', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_10.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_10.xlsx', index=False)
fig_10.plot(x='year', y=['OPPORTUNITY SHARE OF NEW ENTREPRENEURS'])
plt.title("\n".join(wrap("FIGURE 8 OPPORTUNITY SHARE OF NEW ENTREPRENEURS OVER TIME (1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_10.png')

# Figure 11
fig_11 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
fig_11 = kese[(kese['category'] =='Female') | (kese['category'] =='Male') | (kese['category'] =='Total')].reset_index(drop=True)
fig_11 = fig_11[['STATE', 'year', 'category', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_11 = fig_11.pivot_table(index=['year'], columns='category', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
fig_11.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/opp_sex.xlsx', index=False)
fig_11.plot(x='year', y=['Female', 'Male'])
plt.title("\n".join(wrap("FIGURE 9 OPPORTUNITY SHARE OF NEW ENTREPRENEURS BY SEX (1998–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_11.png')

# Figure 12
fig_12 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
fig_12 = kese[(kese['category'] =='White') | (kese['category'] =='Black') | (kese['category'] =='Asian') |\
             (kese['category'] =='Latino') | (kese['category'] =='Total')].reset_index(drop=True)
fig_12 = fig_12[['STATE', 'year', 'category', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_12 = fig_12.pivot_table(index=['year'], columns='category', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
fig_12.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/opp_race.xlsx', index=False)
fig_12.plot(x='year', y=['White', 'Asian', 'Black', 'Latino'])
plt.title("\n".join(wrap("FIGURE 10 OPPORTUNITY SHARE OF NEW ENTREPRENEURS BY RACE AND ETHNICITY (1998–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_12.png')

# Figure 13
fig_13 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
fig_13 = kese[(kese['category'] =='Native-Born') | (kese['category'] =='Immigrant') | (kese['category'] =='Total')].reset_index(drop=True)
fig_13 = fig_13[['STATE', 'year', 'category', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_13 = fig_13.pivot_table(index=['year'], columns='category', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
fig_13.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/opp_nativity.xlsx', index=False)
fig_13.plot(x='year', y=['Immigrant', 'Native-Born'])
plt.title("\n".join(wrap("FIGURE 11 OPPORTUNITY SHARE OF NEW ENTREPRENEURS BY NATIVITY(1998–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_13.png')

# Figure 14
fig_14 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
fig_14 = kese[(kese['category'] =='Ages 20-34') | (kese['category'] =='Ages 35-44') | (kese['category'] =='Ages 45-54') |\
             (kese['category'] =='Ages 55-64') | (kese['category'] =='Total')].reset_index(drop=True)
fig_14 = fig_14[['STATE', 'year', 'category', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_14 = fig_14.pivot_table(index=['year'], columns='category', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
fig_14.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/opp_age.xlsx', index=False)
fig_14.plot(x='year', y=['Ages 20-34', 'Ages 35-44', 'Ages 45-54', 'Ages 55-64'])
plt.title("\n".join(wrap("FIGURE 12 OPPORTUNITY SHARE OF NEW ENTREPRENEURS BY AGE (1998–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_14.png')

# Figure 15
fig_15 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
fig_15 = kese[(kese['category'] =='Less than High School') | (kese['category'] =='High School Graduate') | (kese['category'] =='Some College') |\
             (kese['category'] =='College Graduate') | (kese['category'] =='Total')].reset_index(drop=True)
fig_15 = fig_15[['STATE', 'year', 'category', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_15 = fig_15.pivot_table(index=['year'], columns='category', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
fig_15.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/opp_edu.xlsx', index=False)
fig_15.plot(x='year', y=['Less than High School', 'High School Graduate', 'Some College', 'College Graduate'])
plt.title("\n".join(wrap("FIGURE 13 OPPORTUNITY SHARE OF NEW ENTREPRENEURS BY EDUCATION (1998–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_15.png')

# Figure 16
fig_16 = kese[(kese['STATE']=='United States')].reset_index(drop=True)
fig_16 = kese[(kese['category'] =='Veterans') | (kese['category'] =='Non-Veterans') | (kese['category'] =='Total')].reset_index(drop=True)
fig_16 = fig_16[['STATE', 'year', 'category', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_16 = fig_16.pivot_table(index=['year'], columns='category', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
fig_16.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/opp_veteran.xlsx', index=False)
fig_16.plot(x='year', y=['Non-Veterans', 'Veterans'])
plt.title("\n".join(wrap("FIGURE 14 OPPORTUNITY SHARE OF NEW ENTREPRENEURS BY VETERAN STATUS (1998–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_16.png')

# Figure 17
fig_17 = kese[(kese['type'] =='Total') & (kese['year']==2019)].reset_index(drop=True)
fig_17 = fig_17[['STATE', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_17.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_17.xlsx', index=False)

# Figure 18
fig_18 = kese[(kese['type'] =='Total') & (kese['STATE']=='South Dakota') | (kese['STATE']=='District of Columbia') | (kese['STATE']=='Maryland')].reset_index(drop=True)
fig_18 = fig_18[['STATE', 'year', 'OPPORTUNITY SHARE OF NEW ENTREPRENEURS']]
fig_18['STATE'] = fig_18['STATE'].str.replace("Maryland", "Median", case = True)
fig_18 = fig_18.pivot_table(index=['year'], columns='STATE', values='OPPORTUNITY SHARE OF NEW ENTREPRENEURS').reset_index()
fig_18.plot(x='year', y=['South Dakota', 'District of Columbia', 'Median'])
plt.title("\n".join(wrap("FIGURE 21 OPPORTUNITY SHARE OF NEW ENTREPRENEURS OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_18.png')



#############################################################################################################################
################################################ STARTUP EARLY JOB CREATION #################################################
#############################################################################################################################

# Figure 19
fig_19 = kese[(kese['STATE'] =='United States') & (kese['type']=='Total')].reset_index(drop=True)
fig_19 = fig_19[['STATE', 'year', 'STARTUP EARLY JOB CREATION']]
fig_19.plot(x='year', y=['STARTUP EARLY JOB CREATION'])
plt.title("\n".join(wrap("FIGURE 15 STARTUP EARLY JOB CREATION OVER TIME (1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,10])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_19.png')

# Figure 20
fig_20 = kese[(kese['type'] =='Total') & (kese['year']==2019)].reset_index(drop=True)
fig_20 = fig_20[['STATE', 'STARTUP EARLY JOB CREATION']]
fig_20.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_20.xlsx', index=False)

# Figure 21
fig_21 = kese[(kese['type'] =='Total') & (kese['STATE']=='South Dakota') | (kese['STATE']=='District of Columbia') | (kese['STATE']=='Alabama')].reset_index(drop=True)
fig_21 = fig_21[['STATE', 'year', 'STARTUP EARLY JOB CREATION']]
fig_21['STATE'] = fig_21['STATE'].str.replace("Alabama", "Median", case = True)
fig_21 = fig_21.pivot_table(index=['year'], columns='STATE', values='STARTUP EARLY JOB CREATION').reset_index()
fig_21.plot(x='year', y=['South Dakota', 'District of Columbia', 'Median'])
plt.title("\n".join(wrap("FIGURE 23 STARTUP EARLY JOB CREATION OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([0,25])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_21.png')

#############################################################################################################################
################################################ STARTUP EARLY SURVIVAL RATE ################################################
#############################################################################################################################

# Figure 22
fig_22 = kese[(kese['STATE'] =='United States') & (kese['type']=='Total')].reset_index(drop=True)
fig_22 = fig_22[['STATE', 'year', 'STARTUP EARLY SURVIVAL RATE']]
fig_22.plot(x='year', y=['STARTUP EARLY SURVIVAL RATE'])
plt.title("\n".join(wrap("FIGURE 16 STARTUP EARLY SURVIVAL RATE OVER TIME (1996–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_22.png')

# Figure 23
fig_23 = kese[(kese['type'] =='Total') & (kese['year']==2019)].reset_index(drop=True)
fig_23 = fig_23[['STATE', 'STARTUP EARLY SURVIVAL RATE']]
fig_23.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_23.xlsx', index=False)

# Figure 24
fig_24 = kese[(kese['type'] =='Total') & (kese['STATE']=='Connecticut') | (kese['STATE']=='Virginia') | (kese['STATE']=='Tennessee')].reset_index(drop=True)
fig_24 = fig_24[['STATE', 'year', 'STARTUP EARLY SURVIVAL RATE']]
fig_24['STATE'] = fig_24['STATE'].str.replace("Tennessee", "Median", case = True)
fig_24 = fig_24.pivot_table(index=['year'], columns='STATE', values='STARTUP EARLY SURVIVAL RATE').reset_index()
fig_24.plot(x='year', y=['Connecticut', 'Virginia', 'Median'])
plt.title("\n".join(wrap("FIGURE 25 STARTUP EARLY SURVIVAL RATE OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([50,100])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_24.png')



#############################################################################################################################
######################################################## KESE INDEX #########################################################
#############################################################################################################################


# Figure 25_26
fig_25_26 = kese[(kese['type'] =='Total') & (kese['year']==2019)].reset_index(drop=True)
fig_25_26 = fig_25_26[['STATE', 'KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX']]
fig_25_26.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_25_26.xlsx', index=False)

plt.close('all')

# Figure 17 and Table 8
fig_7_tab_8 = kese[(kese['type'] =='Total') & (kese['STATE']=='United States')].reset_index(drop=True)
fig_7_tab_8 = fig_7_tab_8[['STATE', 'year', 'KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX']]
fig_7_tab_8.to_excel('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_7_tab_8.xlsx', index=False)
fig_7_tab_8.plot(x='year', y=['KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX'])
plt.title("\n".join(wrap("FIGURE 17 KAUFFMAN EARLY-STAGE ENTREPRENEURSHIP (KESE) INDEX OVER TIME (1998–2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([-10,10])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_7_tab_8.png')

# Figure 27
fig_27 = kese[(kese['type'] =='Total') & (kese['STATE']=='California') | (kese['STATE']=='Connecticut') | (kese['STATE']=='Nebraska')].reset_index(drop=True)
fig_27 = fig_27[['STATE', 'year', 'KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX']]
fig_27['STATE'] = fig_27['STATE'].str.replace("Nebraska", "Median", case = True)
fig_27 = fig_27.pivot_table(index=['year'], columns='STATE', values='KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX').reset_index()
fig_27['year'] = pd.to_datetime(fig_27['year'], format='%Y')
fig_27.plot(x='year', y=['California', 'Connecticut', 'Median'])
plt.title("\n".join(wrap("FIGURE 26 KAUFFMAN EARLY-STAGE ENREPRENEURSHIP (KESE) INDEX OVER TIME (1998–2019) (LOWEST, HIGHEST, AND MEDIAN LEVELS IN 2019)", 50)))
axes = plt.gca()
plt.tight_layout()
axes.set_ylim([-10,10])
plt.savefig('/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/tables_plots/fig_27.png')


