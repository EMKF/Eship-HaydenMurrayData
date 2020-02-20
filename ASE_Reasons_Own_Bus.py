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

# import data
df = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/ASE_2016_reasons_own_business.csv')

# keep vars
df = df[['GEO.display-label', 'NAICS.display-label', 'ASECBO.display-label', 'YIBSZFI.display-label', 'REASONOWN.display-label', 'OWNPDEMP_PCT']]
# Rename columns
df.rename(columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECBO.display-label": "demographic"\
    ,"YIBSZFI.display-label": "firm_age", "REASONOWN.display-label": "reason"},inplace=True)
print(df.head())

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
df_gender = [df_gender['demographic'] == 'Male' or 'Female']
df_gender = df_gender[df_gender['firm_age'] == 'All firms']
df_gender.reset_index(inplace=True, drop=True)
df_gender.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/gender_reasons_own_bus.xlsx', index=False)
print(df_gender)

# observation filter: race
df_race = df[df['region'] == 'United States']
df_race = df_race[df_race['industry'] == 'Total for all sectors']
df_race = df_race[df_race['demographic'] == 'Hispanic' or 'White' or 'Asian' or 'Black or African American']
df_race = df_race[df_race['firm_age'] == 'All firms']
df_race.reset_index(inplace=True, drop=True)
df_race.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/race_reasons_own_bus.xlsx', index=False)
print(df_race)

# df_gender =
# df_race =
    # if demographic == 'all':
    #     df = df.loc[df['ASECBO.display-label'] == "All owners of respondent firms"]
    # elif demographic == 'gender':
    #     df = df.loc[(df['ASECBO.display-label'] == "Male") | (df['ASECBO.display-label'] == "Female")]
    # else:  # race
    #     df = df.loc[
    #         (df['ASECBO.display-label'] == "Hispanic") |
    #         (df['ASECBO.display-label'] == "White") |
    #         (df['ASECBO.display-label'] == "Asian") |
    #         (df['ASECBO.display-label'] == "Black or African American")
    #     ]
    # return df.\
    #     loc[df['YIBSZFI.display-label'] == "All firms"].\
    #     loc[df['NAICS.display-label'] == "Total for all sectors"].\
    #     query('OWNPDEMP_PCT == OWNPDEMP_PCT').\
    #     reset_index(drop=True)
