import pandas as pd
import sys
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# read in data
data = pd.read_csv('/Users/hmurray/Desktop/data/EPOP/survey_documentation/s3_final_epop_dataset.csv', low_memory=False)

# create new datasets to manipulate
data = data.drop(['B18Q286', 'B18Q287', 'Q288'], axis=1)

# export mary's Qs subset
data.to_csv('/Users/hmurray/Desktop/data/EPOP/survey_documentation/mary_removed.csv')

sys.exit()