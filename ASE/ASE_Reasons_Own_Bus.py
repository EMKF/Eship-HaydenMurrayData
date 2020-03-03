import os
import sys
import time
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# KESE - Rate of New Entrepreneurs output
rne = pd.read_csv('/Users/hmurray/Desktop/KESE/KESE_2018_data/KESE_rate.csv')
rne = rne[52:54]
rne.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/rne_gender.xlsx', index=False)

# NEB - Rate of New Employer Businesses output
rneb = pd.read_excel('/Users/hmurray/Desktop/NEB/NEB_Data/FINAL_DATA/NEB_Rate.xlsx')
rneb = rneb[51:52]
rneb.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/rneb_us.xlsx', index=False)

# KESE - OPPORTUNITY SHARE OF ENTREPRENEURS
kese = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/original_pull/KESE_opp.csv')

# United States OSE
kese_us = kese[51:52]
kese_us = kese_us.iloc[:,:26]
kese_us.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/kese_opp_US.xlsx', index=False)
print(kese_us)

# Gender OSE
kese_gender = kese[(kese.demographic == 'Men') | (kese.demographic == 'Women')]
kese_gender = kese_gender.iloc[:,:26]
kese_gender.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/kese_opp_gender.xlsx', index=False)
print(kese_gender)

# Race OSE
kese_race = kese[(kese.demographic == 'White') | (kese.demographic == 'Black')| (kese.demographic == 'Latino') | (kese.demographic == 'Asian')]
kese_race = kese_race.iloc[:,:26]

# standard deviations for OSE
kese_race['std'] = kese_race.std(axis=1)
kese_race['max'] = kese_race.max(axis=1)
kese_race['min'] = kese_race.loc[:, ['ose-1998', 'ose-1999', 'ose-2000', 'ose-2001', 'ose-2002', 'ose-2003', 'ose-2004', 'ose-2005',\
                                     'ose-2006', 'ose-2007', 'ose-2008', 'ose-2009', 'ose-2010', 'ose-2011', 'ose-2012', 'ose-2013',\
                                     'ose-2014', 'ose-2015', 'ose-2016', 'ose-2017', 'ose-2018']].min(axis=1)
print(kese_race)
kese_race.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/kese_opp_race.xlsx', index=False)

# ASE - REASONS WHY ENTREPRENEURS OWN THEIR BUSINESS
# import data
df = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/original_pull/ASE_2016_reasons_own_business.csv')

# keep vars
df = df[['GEO.display-label', 'NAICS.display-label', 'ASECBO.display-label', 'YIBSZFI.display-label', 'REASONOWN.display-label', 'OWNPDEMP_PCT']]
# Rename columns
df.rename(columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECBO.display-label": "demographic"\
    ,"YIBSZFI.display-label": "firm_age", "REASONOWN.display-label": "reason", "OWNPDEMP_PCT": "percent"},inplace=True)

# filter responses
df = df[df['reason'] != 'Other: Not important']
df = df[df['reason'] != 'Other: Somewhat important']
df = df[df['reason'] != 'Other: Very important']
df = df[df['reason'] != 'Total reporting']
df = df[df['reason'] != 'Item not reported']

# observation filter: all
df_all = df[df['region'] == 'United States']
df_all = df_all[df_all['industry'] == 'Total for all sectors']
df_all = df_all[df_all['demographic'] == 'All owners of respondent firms']
df_all = df_all[df_all['firm_age'] == 'All firms']
df_all.reset_index(inplace=True, drop=True)
df_all.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/all_reasons_own_bus.xlsx', index=False)
print(df_all)

# observation filter: gender
df_gender = df[df['region'] == 'United States']
df_gender = df_gender[df_gender['industry'] == 'Total for all sectors']
df_gender = df_gender[(df_gender.demographic == 'Male') | (df_gender.demographic == 'Female')]
df_gender = df_gender[df_gender['firm_age'] == 'All firms']
df_gender.reset_index(inplace=True, drop=True)
df_gender.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/gender_reasons_own_bus.xlsx', index=False)
print(df_gender)

# observation filter: race
df_race = df[df['region'] == 'United States']
df_race = df_race[df_race['industry'] == 'Total for all sectors']
df_race = df_race[(df_race.demographic == 'Hispanic') | (df_race.demographic == 'White') | (df_race.demographic == 'Asian') | (df_race.demographic == 'Black or African American')]
# df_race = df_race[df_race['firm_age'] == 'All firms']
df_race.reset_index(inplace=True, drop=True)
df_race.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/race_reasons_own_bus.xlsx', index=False)
print(df_race)

# observation filter: race very important
df_all_very = df_all[df_all['reason'].str.contains("Very")]
df_all_very.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/very_all_reasons_own_bus.xlsx', index=False)

# observation filter: gender very important
df_gender_very = df_gender[df_gender['reason'].str.contains("Very")]
df_gender_very.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/very_gender_reasons_own_bus.xlsx', index=False)

# observation filter: race very important
df_race_very = df_race[df_race['reason'].str.contains("Very")]
df_race_very.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/very_race_reasons_own_bus.xlsx', index=False)



# transpose OSE
plot_us = kese_us.transpose().iloc[3: ].rename(columns={51:'United States'}).assign(year=range(1996, 2019)).reset_index(drop=True)
plot_gender = kese_gender.transpose().iloc[3: ].rename(columns={53:'Men', 54:'Women'}).assign(year=range(1996, 2019)).reset_index(drop=True)
plot_race = kese_race.transpose().iloc[3:26].rename(columns={55:'White', 56:'Black', 57:'Latino', 58:'Asian'}).assign(year=range(1996, 2019)).reset_index(drop=True)

# U.S. ose plot
def matplotlib_plot(df, outcome_var, save=None):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)
    for var in outcome_var:
        ax.plot('year', var, data=df, label=var)
        ax.set_ylim([.65, .95])
        ax.set_xticks(range(1996, 2019, 2))
    plt.title('Opportunity Share of New Entrepreneurs')
    # plt.suptitle('Opportunity Share of New Entrepreneurs')
    plt.legend()
    if save:
        plt.savefig(save)
    plt.show()

matplotlib_plot(plot_us, ['United States'], '/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/us_ose.png')
gender = ['Men', 'Women']
matplotlib_plot(plot_gender, gender, '/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/gender_ose.png')
race = ['White', 'Black', 'Latino', 'Asian']
matplotlib_plot(plot_race, race, '/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/race_ose.png')

sys.exit()