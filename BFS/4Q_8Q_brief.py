import sys
import pandas as pd
from kauffman_data import bfs, pep
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.f' % x)
pd.options.mode.chained_assignment = None


# BFS
bfs = bfs.get_data(['BA_BA', 'BF_SBF4Q', 'BF_SBF8Q'], 'us', 2005, end_year=2019, annualize=False)
bfs['Period'] = bfs['Period'].astype(str).str[:-2].astype(np.int64)
bfs = bfs.groupby('Period').sum().reset_index()
print(bfs)

# Pep
pep = pep.get_data('us', 2005, 2018)
print(pep)

# df.plot(x='Period', y=['BF_SBF8Q', 'BF_SBF4Q'])
# plt.show()

