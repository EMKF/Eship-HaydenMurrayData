import pandas as pd
import os
import sys
import requests
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.f' % x)
pd.options.mode.chained_assignment = None




df = pd.read_csv('s3://emkf.data.research/other_data/database_USA/heartland_msa_businesses.csv')
print(df.head())