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
searches = ('US_business_loan_90days', 'US_self_employed_90', 'US_open_bus_5_years', 'US_small_bus_5_years', 'US_bus_app_5_years')
trends = {}
for x in searches:
    trends[x] = pd.read_csv('/Users/hmurray/Desktop/data/google/google_data/' + str(x) + '.csv', skiprows=2)
    print(trends[x].head())

def trender(dict, time, col):
    dict.plot(x=time, y=col)
    plt.title(col)
    plt.savefig('/Users/hmurray/Desktop/data/google/google_data/plots/' + str(col) + '.png')
    plt.show()

trender(trends['US_business_loan_90days'], 'Day', 'business loan: (United States)')
trender(trends['US_self_employed_90'],'Day', 'self employed: (United States)')
trender(trends['US_open_bus_5_years'], 'Week', 'open a business: (United States)')
trender(trends['US_small_bus_5_years'], 'Week', 'small business: (United States)')

sys.exit()

