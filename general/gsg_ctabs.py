# data was provided by Jessica on June 3rd, 2020

import pandas as pd
import sys
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# read in data
all_df = pd.read_csv('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/raw_gsg_6.3.csv')
print(all_df.head())

# create new datasets
# young_df = all_df.loc[all_df['Q4']==1]
# old_df = all_df.loc[all_df['Q4']!=1]
# closed = all_df.loc[all_df['Q2']==2]
# opened = all_df.loc[all_df['Q2']==1]

# categorize Q4 (years in business) by YOUNG, OLD
all_df.loc[all_df['Q4'] != 1, 'Q4'] = 2

# rename Q2 and Q4
all_df['Q2'] = all_df['Q2'].astype(str).replace(str(1), 'Still in business').replace(str(2), 'It has closed')
all_df['Q4'] = all_df['Q4'].astype(str).replace(str(1), 'YOUNG').replace(str(2), 'OLD')
all_df['Q56_15_1'] = all_df['Q56_15_1'].astype(str).replace(str(1), 'temp_closed').replace(str(0), 'did_not_close')

# create priority tab list and rename via for loop
structure_list = ['Q7', 'Q8', 'Q9']
for x in structure_list:
    all_df[x] = all_df[x].astype(str).replace(str(1), '1 Just myself and co-owners, no other employees').replace(str(2), '2 1-10')\
.replace(str(3), '3 11-50').replace(str(4), '4 51-100').replace(str(5), '5 More than 100')
print(pd.crosstab(all_df['Q4'], all_df['Q7']))

# Create a Pandas Excel writer using XlsxWriter as the engine.
priorities_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/all_ctabs_priorities.xlsx', engine='xlsxwriter')

# prep crosstabs
freq = pd.DataFrame()
ctabs = pd.DataFrame()
def crosser(df, var, writer):
    print()
    freq = pd.crosstab(df[var], df[var], values=df['WEIGHT'], aggfunc='sum', normalize='columns', margins=True)
    freq.rename(columns={"All": var},inplace=True)
    freq = freq[var]
    print(freq)
    print()
    two = pd.crosstab(df[var], df['Q56_15_1'], values=df['WEIGHT'], aggfunc='sum', normalize='columns', margins=True)
    print(two)
    print()
    # priorities = pd.crosstab(all_df[var], [all_df['Q4'], all_df['Q56_15_1']], values=all_df['WEIGHT'], aggfunc='sum')
    priorities = pd.crosstab(all_df['Q56_15_1'], [all_df['Q4'], all_df[var]], values=all_df['WEIGHT'], aggfunc='sum')
    priorities = priorities.transpose().reset_index(drop=False)
    print(priorities)
    priorities.to_excel(writer, sheet_name=str(var), index=True)

tab_list = ['Q7', 'Q8', 'Q9']
for x in tab_list:
    crosser(all_df, x, priorities_writer)

priorities_writer.save()
sys.exit()

