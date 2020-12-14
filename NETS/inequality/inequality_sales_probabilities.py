# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp91 and empc91 tells you employees in business in 1990

import pandas as pd
import numpy as np
import time
import sys
import dask.dataframe as dd

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# time
start = time.time()

# pull sales data from S3
sales = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Sales_Ratings/NETS2017_Sales.txt',\
            sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1', nrows=500)
print(sales.head())

# how long did it take to run?
print((time.time() / 60) - (start / 60))
sys.exit()