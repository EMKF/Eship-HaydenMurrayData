import sys
import pandas as pd
from kauffman_data import bfs, pep
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None


# 4Q & 8Q Actualization
df = bfs.get_data(['BA_BA', 'BF_SBF4Q', 'BF_SBF8Q'], 'us', 2005, end_year=2019, annualize=False)
df['Period'] = df['Period'].astype(str).str[:-2].astype(np.int64)
df = df.groupby('Period').sum().reset_index()
df['4Q_actualization'] = (df['BF_SBF4Q']/df['BA_BA'])*100
df['8Q_actualization'] = (df['BF_SBF8Q']/df['BA_BA'])*100
print(df)
sys.exit()
