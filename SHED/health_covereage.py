# data downloaded manually from: https://www.federalreserve.gov/consumerscommunities/shed_data.htm

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None


# pull,
data = pd.read_csv('/Users/hmurray/Desktop/data/SHED/2018_SHED_data.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# subset
df = data[['E2A']]


