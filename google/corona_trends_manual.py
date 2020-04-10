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
searches = ('US_business_loan_90days', 'US_self_employed_90')
for x in searches:
    pd.read_csv('/Users/hmurray/Desktop/data/google/google_data/' + str(x) + '.csv', skiprows=2)
    print()




# # plot
# df.plot(x='Day', y='business loan: (United States)')
# plt.title('US_business_loan_90days')
# plt.savefig('/Users/hmurray/Desktop/data/google/google_data/' + str(x) + '.png')
# plt.show()


