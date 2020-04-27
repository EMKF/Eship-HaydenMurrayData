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
dir = '/Users/hmurray/Desktop/data/KESE/share_total/tables/agg/agg_share_tables.xlsx'
# read in data
kese = ('race', 'gender', 'veteran', 'nativity', 'age', 'edu')
share = {}
for x in kese:
    share[x] = pd.read_excel(dir, sheet_name=str(x))
    print(share[x].head())

def trender(share, col, title):
    share.plot(x='year', y=col)
    plt.title(title)
    plt.savefig('/Users/hmurray/Desktop/data/KESE/share_total/plots/agg/' + str(title) + '.png')
    plt.show()
race = ['White', 'White-Opp', 'Black', 'Black-Opp', 'Latino', 'Latino-Opp', 'Asian', 'Asian-Opp']
trender(share['race'], race, 'Share of New and Opportunity Entrepreneurs by Race and Ethnicity')

