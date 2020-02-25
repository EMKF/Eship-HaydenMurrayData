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


# load PEP data
pep = pd.read_csv('/Users/hmurray/Desktop/data/PEP/PEP_2018_PEPSR6H.csv')

# filter for United States, both sexes, 2016
pep = pep[(pep.Geography == 'United States')]
pep = pep[(pep.Sex == 'Both Sexes')]
pep = pep[(pep.Year == '1-Jul-16')]
pep.reset_index(inplace=True, drop=True)

# sum hispanic, + minority categories
pep['2016'] = pep['Total'] + pep['Black or African American'] + pep['American Indian and Alaska Native'] + pep['Asian']\
              + pep['Native Hawaiin and Other Pacific Islander'] + pep['Two or More Races']
pep.to_excel('/Users/hmurray/Desktop/data/PEP/PEP_demo.xlsx', index=False)
print(pep)

# save white population
white = pep.iloc[1,10]
print(white)
# save total population
total = pep.iloc[2,9]
print(total)
# save minority population
min = total - white
print(min)
# white percent
white_per = (white/total)*100
print(white_per)
# minority percent
min_per = (min/total)*100
print(min_per)