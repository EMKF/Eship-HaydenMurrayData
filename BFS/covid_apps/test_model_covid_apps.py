# YouTube: https://www.youtube.com/watch?v=9Kc5vuC48ME

import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from matplotlib import pyplot as plt

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# read in all BFS data
df = pd.read_excel('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/2021/updated_data/covid_bfs_industry.xlsx')
print(df.head())

# filter for dates and naics
df = df[(df['industry'] == 'All NAICS Sectors')]

# drop columns
df = df[['time', 'BA_BA', 'BA_WBA']]

# drop NaN
df.dropna(axis=0, inplace=True)

# set index as time
df.set_index('time', inplace=True)
print(df.head())

# plot to see trend
df.plot()
plt.show()

# create model
sarimax_model = SARIMAX(df['BA_BA'], order=(1,1,1), seasonal_order=(1,1,1,4), exog=df['BA_WBA'])
res = sarimax_model.fit(disp=False)
print(res.summary())


