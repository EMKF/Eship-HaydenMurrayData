import os
import pandas as pd
from kauffman.data import bfs, bds, pep
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('chained_assignment',None)

df = bfs(series_lst=['BA_BA', 'BF_SBF8Q'], obs_level='us', industry='00', seasonally_adj=True, annualize=True, march_shift=False)
print(df.head())
print(df.tail())
df.to_excel('/Users/hmurray/Desktop/NEB/2021/data/national_report/ba_reference.xlsx')
sys.exit()
#
# df = pep('all')
# print(df)

# df = pd.read_csv('https://www.census.gov/econ/bfs/csv/bfs_quarterly.csv')
# print(df)
# df.to_excel('/Users/hmurray/Desktop/bfs_test.xlsx')

# df = pd.read_csv('https://www.census.gov/econ/bfs/csv/bfs_monthly.csv')
# df = df[(df.naics_sector == 'TOTAL').reset_index(drop=True)]
#
# print(df)

# df = bds(series_lst=['ESTAB'], obs_level='all', strata=[], get_flags=False, census_key=os.getenv('CENSUS_KEY'), n_threads=1)
# print(df.head())


# df = pd.read_csv('https://www.census.gov/econ/bfs/csv/bfs_quarterly.csv')
# df[pd.to_numeric(df['Q1'], errors='coerce').notnull()]
# df[pd.to_numeric(df['Q2'], errors='coerce').notnull()]
# df[pd.to_numeric(df['Q3'], errors='coerce').notnull()]
# df[pd.to_numeric(df['Q4'], errors='coerce').notnull()]
# df[['Q1', 'Q2', 'Q3', 'Q4']] = df[['Q1', 'Q2', 'Q3', 'Q4']].astype(int)
# df.to_excel('/Users/hmurray/Desktop/bfs_test.xlsx')
# print(df.head())
