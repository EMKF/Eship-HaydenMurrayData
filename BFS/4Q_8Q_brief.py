import sys
import pandas as pd
from kauffman_data import bfs, pep
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.5f' % x)
pd.options.mode.chained_assignment = None


# BFS
bfs = bfs.get_data(['BA_BA', 'WBA_BA', 'BF_SBF4Q', 'BF_SBF8Q'], 'us', 2005, end_year=2019, annualize=False)
bfs['time'] = bfs['time'].astype(str).str[:-2].astype(np.int64)
bfs = bfs.groupby('time').sum().reset_index()

# Pep
pep = pep.get_data('us', 2005, 2018)
pep.rename(columns={"year": "time"},inplace=True)

# merge bfs and pep
data = pd.merge(bfs, pep, on=['time'])

# population adjustment
data['BF8Q_POP'] = (data['BF_SBF8Q']/data['population'])*100000
data['BF4Q_POP'] = (data['BF_SBF4Q']/data['population'])*100000
data['WBA_POP'] = (data['WBA_BA']/data['population'])*100000
data['BA_POP'] = (data['BA_BA']/data['population'])*100000
print(data)

# plot 'em
data.plot(x='time', y=['BF4Q_POP', 'BF8Q_POP', 'WBA_POP', 'BA_POP'])
plt.xlabel('Year')
plt.xticks(rotation=45)
plt.ylabel('Number per 100,000 people')
plt.legend(title='BFS Variables (population adjusted)')
title = ('Business Applications, Wage-Based Business Applications, 4-Quarter Business Formations, 8-Quarter Business Formations')
plt.title("\n".join(wrap(title, 65)))
plt.tight_layout()
plt.savefig('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/ba_wba_4bf_8bf.png')
plt.show()

