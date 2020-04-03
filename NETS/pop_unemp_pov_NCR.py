# pop data downloaded manually from: https://data.ers.usda.gov/reports.aspx?ID=17827
# unemp data downloaded manually from: https://data.ers.usda.gov/reports.aspx?ID=17828
# pov data downloaded manually from: https://data.ers.usda.gov/reports.aspx?ID=17826

import os
import sys
import shutil
import xlrd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
from textwrap import wrap
from kauffman_data import bfs, pep

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None


#########################################################################################################################
############################################## IRS SELF-EMPLOYMENT ANALYSIS #############################################
#########################################################################################################################

# pull county level self-employment
self = pd.read_csv('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/pop_unemp_pov_NCR/IRSSelfEmployment (1).csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# slice df for total returns and returns with self-employment
self = self[['county', 'year', 'AGI', 'State', 'Returns', 'Returns_with_Self_Tax']]

# groupby
self = self.groupby(['county', 'year', 'AGI'])['Returns', 'Returns_with_Self_Tax'].agg('sum').reset_index()

# filter, reset index, take a look
self = self.loc[(self.county == 11001) | (self.county == 24031) | (self.county == 24033) |\
            (self.county == 51013) | (self.county == 51059) | (self.county == 51107) | (self.county == 51153)]
self.reset_index(inplace=True)

# calculate
returns = self.groupby(['county', 'year'])['Returns'].agg('sum').reset_index()
print(returns)
with_tax = self.groupby(['county', 'year'])['Returns_with_Self_Tax'].agg('sum').reset_index()
print(with_tax)
self = pd.merge(returns, with_tax, on=['county', 'year'])
self['percent_returns_self_emp'] = (self['Returns_with_Self_Tax']/self['Returns'])*100
print(self)


#########################################################################################################################
################################################ POP, UNEMP, POV ANALYSIS ###############################################
#########################################################################################################################

# pull sjc  and NEB
pop = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/pop_unemp_pov_NCR/pop_unemp_pov_NCR.xlsx', sheet_name='Population')
unemp = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/pop_unemp_pov_NCR/pop_unemp_pov_NCR.xlsx', sheet_name='Unemployment')
pov = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/pop_unemp_pov_NCR/pop_unemp_pov_NCR.xlsx', sheet_name='Poverty')

def _filter(df):
    df = df[(df.County == 'District of Columbia') | (df.County == 'Montgomery County')| (df.County == 'Prince George\'s County') | (df.County == 'Arlington County') |\
            (df.County == 'Fairfax County') | (df.County == 'Loudoun County') | (df.County == 'Prince William County')]
    df.reset_index(drop=True, inplace=True)
    return df

pop = _filter(pop)
unemp = _filter(unemp)
pov = _filter(pov)

# rename unemp columns
# unemp.rename(columns={"2010": "Unemployment 2010", "2018": "Unemployment 2018"},inplace=True)
pov.rename(columns={"Percent": "Percent in Poverty"},inplace=True)

print(pop.head())
print(unemp.head())
print(pov.head())

# concat, subset, export table 1
df = pd.concat([pop,unemp,pov],sort=True, axis=1)
df = df[['County', 'FIPS*', 'Pop. 2010',  'Pop. 2018' , 'Change 2010-18', 'Median Household Income (2018)', '% of State Median HH Income', 'Percent in Poverty']]
data = df.iloc[:, np.r_[2, 4:11]]

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/percent_returns_self_emp.xlsx', engine='xlsxwriter')

# export self-employment data
self.to_excel(writer, sheet_name='self_emp_tax', index=False)

# export table 1 to excel sheet 1
data.to_excel(writer, sheet_name='pop_unemp_pov', index=False)

# subset and export unemp data for table 2
unemp = unemp.iloc[:, np.r_[0:11]]

# export table 2 to excel sheet 2
unemp.to_excel(writer, sheet_name='unemployment', index=False)

# save and closer writer
writer.save()

sys.exit()