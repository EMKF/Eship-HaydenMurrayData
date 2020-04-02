# ba data downloaded from KCR library, saved locally, and imported manually

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
############################################# BUSINESS APPLICATIONS ANALYSIS ############################################
#########################################################################################################################

# pull ba from KCR BFS local library
state_BA = pd.read_excel('/Users/hmurray/Desktop/data/BFS/BA/ba.xlsx', sheet_name='state_BA')
adj_ba = pd.read_excel('/Users/hmurray/Desktop/data/BFS/BA/ba.xlsx', sheet_name='adj_ba')

# filter for DC, MD, VA
def filterer(df):
    df = df[(df.region == 'DC') | (df.region == 'MD') | (df.region == 'VA')]
    df.reset_index(drop=True, inplace=True)
    return df

state_BA = filterer(state_BA)
adj_ba = filterer(adj_ba)
print(state_BA)
print(adj_ba)

# unstack state_BA
state_BA = state_BA.pivot(index='year', columns='region', values='BA_BA')
state_BA.reset_index(inplace = True)
print(state_BA)

# unstack adj_ba
adj_ba = adj_ba.pivot(index='year', columns='region', values='ba_pop')
adj_ba.reset_index(inplace = True)
print(adj_ba)

# plot ba for NCR states
def plotter(df, var, title, save):
    df.plot(x='year', y=var)
    plt.title("\n".join(wrap(title, 50)))
    plt.xlabel('Year')
    plt.ylabel(title)
    plt.savefig(save)
    plt.tight_layout()
    plt.show()

var = ['DC', 'MD', 'VA']
title1 = "Business Applications - NCR"
title2 = "Business Applications - NCR (adjusted for population)"
plotter(state_BA, var, title1, '/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/ba_NCR.png')
plotter(adj_ba, var, title2, '/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/adj_ba_NCR.png')

sys.exit
