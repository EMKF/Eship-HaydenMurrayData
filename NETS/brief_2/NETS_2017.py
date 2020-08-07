# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp90 and empc90 tells you

import pandas as pd
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull from S3
df = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Misc/NETS2017_Misc.txt',\
                 sep='\t', lineterminator='\r', error_bad_lines=False, encoding='latin1')

# subset
df = df[['DunsNumber', 'FipsCounty', 'FirstYear']]

# create state_fips
df['hm_county_fips'] = df['FipsCounty'].astype(str).str.zfill(5)
df['state_fips'] = df['hm_county_fips'].astype(str).str[:2]
print(df.head())
print(df.info())

# value_counts
print(df['state_fips'].value_counts())
counts = (df.groupby(["state_fips", "FirstYear"]).size())
counts = counts.reset_index()
counts.rename(columns = {0:'est_count'}, inplace = True)
print(counts)
counts.to_excel('/Users/hmurray/Desktop/data/NETS/st_est_counts.xlsx', index=False)
sys.exit()



