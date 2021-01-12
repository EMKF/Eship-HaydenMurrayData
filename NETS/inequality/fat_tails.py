import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
import numpy as np
import time
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# time
start = time.time()

# pull sales data for each year
sales2013 = pd.read_csv('s3://emkf.data.research/sandbox/sales_2013.txt', low_memory=False, nrows=50000)
print(sales2013.describe())
print(sales2013.head())
# sys.exit()
# sales2013 = pd.read_csv('/Users/hmurray/Downloads/sales_2013.txt', low_memory=False, nrows=10000)
# print(sales2013.head())


sales2013['Sales13'].hist(bins=5)
title = 'Distribution of Sales in year _______'
plt.title("\n".join(wrap(title, 50)))
plt.xlim(xmin=-0, xmax = 3500000)
plt.savefig('/Users/hmurray/Desktop/data/NETS/inequality/fat_tails/sales2013.png')
plt.show()

# how long did it take to run?
seconds = time.time() - start
print(seconds)
sys.exit()

