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
dir = '/Users/hmurray/Desktop/data/KESE/share_total/agg_share_tables.xlsx'
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
gender = ['Male_RNE', 'Male_OSE', 'Female_RNE', 'Female_OSE']
veteran = ['Veterans-RNE', 'Veterans-Opp', 'Non-Veterans', 'Non-Veterans-Opp']
nativity = ['Native_Born_RNE', 'Native_Born_OSE', 'Immigrant_RNE', 'Immigrant_OSE']
age = ['20_34_RNE', '20_34_OSE', '35_44_RNE', '35_44_OSE', '45_54_RNE', '45_54_OSE', '55_64_RNE', '55_64_OSE']
edu = ['Less than High School RNE', 'Less than High School OSE', 'High School Graduate RNE', 'High School Graduate OSE',\
       'Some College RNE', 'Some College OSE', 'College Graduate RNE', 'College Graduate OSE']
trender(share['race'], race, 'Share of New and Opportunity Entrepreneurs by Race and Ethnicity')
trender(share['gender'], gender, 'Share of New and Opportunity Entrepreneurs by Gender')
trender(share['veteran'], veteran, 'Share of New and Opportunity Entrepreneurs by Veteran Status')
trender(share['nativity'], nativity, 'Share of New and Opportunity Entrepreneurs by Nativity')
trender(share['age'], age, 'Share of New and Opportunity Entrepreneurs by Age')
trender(share['edu'], edu, 'Share of New and Opportunity Entrepreneurs by Edu')