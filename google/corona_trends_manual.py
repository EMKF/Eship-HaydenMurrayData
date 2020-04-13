# data downloaded manually from: https://trends.google.com/trends/explore?date=all&geo=US&q=business%20loan

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
import pytrends
from pytrends.request import TrendReq

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None

# pull google data
searches = ('new_business_loan_year', 'new_self_employed_year', 'open_bus_year', 'new_small_business_year')
trends = {}
for x in searches:
    trends[x] = pd.read_csv('/Users/hmurray/Desktop/data/google/google_data/' + str(x) + '.csv', skiprows=2)
    print(trends[x].head())

def trender(dict, time, col):
    dict.plot(x=time, y=col)
    plt.title(col)
    plt.savefig('/Users/hmurray/Desktop/data/google/google_data/plots/' + str(col) + '.png')
    plt.show()

trender(trends['new_business_loan_year'], 'Week', 'new business loan: (United States)')
trender(trends['new_self_employed_year'],'Week', 'new self employed: (United States)')
trender(trends['open_bus_year'], 'Week', 'open a business: (United States)')
trender(trends['new_small_business_year'], 'Week', 'new small business: (United States)')

sys.exit()

