# data obtained from https://ledextract.ces.census.gov/static/data.html

import os
import sys
import csv
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
pd.set_option('display.float_format', lambda x: '%.f' % x)
pd.options.mode.chained_assignment = None


# pull data
df = pd.read_csv('/Users/hmurray/Desktop/data/QWI/QWI_net_jobs.csv')

# subset
df = df[['year', 'quarter', 'FrmJbC']]

# groupby year
df = df.groupby(['year'])['FrmJbC'].agg('sum').reset_index()

print(df)






