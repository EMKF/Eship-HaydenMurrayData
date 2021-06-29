# data downloaded manually from: https://www.federalreserve.gov/consumerscommunities/shed_data.htm

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None



mei = pd.read_excel('/Users/hmurray/Desktop/data/SHED/2018_shed/2018_SHED_data.csv')
print(mei)
sys.exit()


















# pull,
data = pd.read_csv('/Users/hmurray/Desktop/data/SHED/2018_shed/2018_SHED_data.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# replace "Refused" with NaN
data.replace('Refused', np.nan, inplace=True)
data.replace('Other (Please specify):', np.nan, inplace=True)

# shorten strings
data['D3A'] = data['D3A'].str.replace("For a single company or employer", "Employed", case = True)
data['D3A'] = data['D3A'].str.replace("For yourself or your family business", "Family- or Self-Employed", case = True)

# subset using startswith()
df = data[data.columns[pd.Series(data.columns).str.startswith(('D3A', 'ppcm1301', 'pph10001', 'FL0', 'E1', 'E2', 'E4'))]]
# print(df.head())

# crosstabs
new = pd.DataFrame()
def crosser(var, save=None):
    print(var.value_counts(normalize=True))
    new = (pd.crosstab([var], df['D3A'], normalize='columns')).round(4) * 100
    print(new)
    return new
    # if save:
    #     new.to_excel(save, index=True)

# names = list(df.columns.values)
df1 = pd.DataFrame()
for x in df:
    df1 = df1.append(crosser(df[x], '/Users/hmurray/Desktop/data/SHED/health_coverage/D3A' + str(x) + '.xlsx'))
print(df1)

sys.exit()

######## ADD THIS TO FOR LOOP ABOVE
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/SHED/health_coverage/D3A' + str(x) + '.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')
df3.to_excel(writer, sheet_name='Sheet3')

# Close the Pandas Excel writer and output the Excel file.
writer.save()