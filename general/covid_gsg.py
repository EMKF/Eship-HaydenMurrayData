# data was provided by Jessica on May 29th, 2020

import pandas as pd
import sys
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# read in data
df = pd.read_csv('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/raw_gsg_5.26.csv')
print(df.head())

# create list of column names that contain 'B', 'Q', or 'D'
names = [column for column in df.columns.tolist() if column[0] in ['B', 'Q', 'D']]

df_weight = df.astype(dict(zip(names, ['str'] * len(names))))
for x in names:
    df_weight[x] = df_weight[x].str.strip().replace('', np.nan).astype(float) * df_weight['WEIGHT']
df_weight['DRACE'] = df_weight['DRACE'] / df_weight['WEIGHT']
print(df_weight.head())
df_weight.to_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/weighted_gsg_5.26.xlsx')
sys.exit()