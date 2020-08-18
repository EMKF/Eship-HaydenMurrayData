import pandas as pd
import sys
from kauffman_data import bfs, pep, lfs, bds

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull
df = pep.get_data('state', 2004, 2018)
print(df)

# save locally
df.to_excel('/Users/hmurray/Desktop/data/PEP/state_pep_2004_2018/state_pep_2004_2018.xlsx', index=False)