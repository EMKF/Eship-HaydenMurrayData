import pandas as pd
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

df = pd.read_csv('s3://emkf.data.research/other_data/chmura/rti_databaseUSA_2020-07-08.csv')
print(df.head())
print(df.info())