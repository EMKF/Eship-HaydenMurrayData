# data downloaded manually from: https://indicators.kauffman.org/data-downloads

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None


# pull sjc  and NEB
data = pd.read_csv('/Users/hmurray/Desktop/KESE/KESE_2018_data/KESE_jobs.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)
act = pd.read_excel('/Users/hmurray/Desktop/NEB/NEB_Data/archive/Alley_Formatted_NEB_Data/attempts/Final_Neb_Data_Seperate_Tabs.xlsx', sheet_name='NEW-EMP BUSINESS ACTUALIZATION')
vel = pd.read_excel('/Users/hmurray/Desktop/NEB/NEB_Data/archive/Alley_Formatted_NEB_Data/attempts/Final_Neb_Data_Seperate_Tabs.xlsx', sheet_name='NEW-EMPLOYER BUSINESS VELOCITY')
new = pd.read_excel('/Users/hmurray/Desktop/NEB/NEB_Data/archive/Alley_Formatted_NEB_Data/attempts/Final_Neb_Data_Seperate_Tabs.xlsx', sheet_name='EMPLOYER BUSINESS NEWNESS')

# format each df
data.columns = data.columns.str.replace('sjc-', '')
data = data.loc[:, data.columns.str.contains('jobs') == False]
sjc = data.loc[:, data.columns.str.contains('pop') == False]

def renamer(df):
    df.rename( columns={'Unnamed: 0':'region'}, inplace=True )
    return df
renamer(act)
renamer(vel)
renamer(new)

# check dfs
print(sjc.head())
print(act.head())
print(vel.head())
print(new.head())
sys.exit()

# filter
def filterer(df):
    df1 = data[(data.region == 'District of Columbia') | (data.region == 'United States')| (data.region == 'Virginia')| (data.region == 'Maryland')]
    df1.reset_index(drop=True, inplace=True)
    return df1

# rename columns
df1.rename(columns={'region': 'Year'}, inplace=True)

# transpose
sjc = df1.transpose()
sjc.reset_index(inplace=True)

# reset columns
sjc.columns = ['Year', 'District of Columbia', 'Maryland', 'Virginia', 'United States']

# drop other rows
sjc = sjc[1:24]
sjc.reset_index(inplace=True)

# trim year column
sjc['Year'] = sjc['Year'].map(lambda x: x.lstrip('sjc-').rstrip('aAbBcC'))

### Other data

# # filter
# neb = neb1[(neb1.Region == 'District of Columbia') | (neb1.Region == 'United States')| (neb1.Region == 'Virginia')| (neb1.Region == 'Maryland')]
# neb.reset_index(drop=True, inplace=True)
# print(neb)


sys.exit()
def plotter(df, var, title, save):
    df.plot(x='Year', y=var)
    plt.title("\n".join(wrap(title, 50)))
    plt.xlabel('Year')
    plt.ylabel(title)
    plt.savefig(save)
    plt.tight_layout()
    plt.show()

var = ['District of Columbia', 'United States', 'Maryland', 'Virginia']
sjc_title = "Startup Job Creation"
act_title = "New Employer Business Actualization"
velocity_title = "New Employer Business Velocity"
newness_title = "New Employer Business Newness"

plotter(sjc, var, sjc_title, '/Users/hmurray/Desktop/Data_Briefs/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/sjc_DC.png')
plotter(neb['NEW-EMPLOYER BUSINESS ACTUALIZATION'], var, act_title, '/Users/hmurray/Desktop/Data_Briefs/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/act_DC.png')