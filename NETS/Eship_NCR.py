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
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None


# pull sjc  and NEB
data = pd.read_csv('/Users/hmurray/Desktop/KESE/KESE_2018_data/KESE_jobs.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)
act = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/neb_pulls/Final_Neb_Data_Seperate_Tabs.xlsx', sheet_name='NEW-EMP BUSINESS ACTUALIZATION')
vel = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/neb_pulls/Final_Neb_Data_Seperate_Tabs.xlsx', sheet_name='NEW-EMPLOYER BUSINESS VELOCITY')
new = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/neb_pulls/Final_Neb_Data_Seperate_Tabs.xlsx', sheet_name='EMPLOYER BUSINESS NEWNESS')

# format each df
data.columns = data.columns.str.replace('sjc-', '')
data = data.loc[:, data.columns.str.contains('jobs') == False]
sjc = data.loc[:, data.columns.str.contains('pop') == False]

def renamer(df):
    df.rename( columns={'Unnamed: 0':'region'}, inplace=True )
    df.sort_values(by=['region'], ascending=True)
    return df
renamer(act)
renamer(vel)
renamer(new)

def _filter(df):
    df = df[(df.region == 'District of Columbia') | (df.region == 'United States')| (df.region == 'Virginia')| (df.region == 'Maryland')]
    df.reset_index(drop=True, inplace=True)
    df.rename(columns={'region': 'Year'}, inplace=True)
    df = df.transpose()
    df.reset_index(inplace=True)
    df.columns = df.iloc[0]
    df = df.reindex(df.index.drop(0)).reset_index(drop=True)
    return df

sjc = _filter(sjc)
act = _filter(act)
vel = _filter(vel)
new = _filter(new)

def calculator(df):
    df["District of Columbia"] = 100 * df["District of Columbia"]
    df["Maryland"] = 100 * df["Maryland"]
    df["Virginia"] = 100 * df["Virginia"]
    df["United States"] = 100 * df["United States"]
calculator(act)
calculator(new)

print(sjc.head())
print(act.head())
print(vel.head())
print(new.head())




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

plotter(sjc, var, sjc_title, '/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/sjc_DC.png')
plotter(act, var, act_title, '/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/act_DC.png')
plotter(vel, var, velocity_title, '/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/vel_DC.png')
plotter(new, var, newness_title, '/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/new_DC.png')