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

# categorize, rename Q4 (years in business) by YOUNG, OLD
all_df.loc[all_df['Q4'] != 1, 'Q4'] = 2
all_df['Q4'] = all_df['Q4'].astype(str).replace(str(1), 'YOUNG').replace(str(2), 'OLD')

# rename Q2
all_df['Q2'] = all_df['Q2'].astype(str).replace(str(1), 'Still in business').replace(str(2), 'It has closed')
test = pd.crosstab(all_df['Q4'], [all_df['Q2'], all_df['Q7']], values=all_df['WEIGHT'], aggfunc='sum', normalize='columns')
print(test)

sys.exit()

young_df = all_df.loc[all_df['Q4']==1]
old_df = all_df.loc[all_df['Q4']!=1]
closed = all_df.loc[all_df['Q2']==2]
opened = all_df.loc[all_df['Q2']==1]

# Create a Pandas Excel writer using XlsxWriter as the engine.
all_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/all_ctabs_priorities.xlsx', engine='xlsxwriter')
young_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/young_ctabs_priorities.xlsx', engine='xlsxwriter')
old_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/old_ctabs_priorities.xlsx', engine='xlsxwriter')
closed_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/closed_ctabs_priorities.xlsx', engine='xlsxwriter')
opened_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/opened_ctabs_priorities.xlsx', engine='xlsxwriter')

# prep crosstabs
freq = pd.DataFrame()
ctabs = pd.DataFrame()

def crosser(df, var, writer, title):
    print()
    freq = pd.crosstab(df[var], df[var], values=df['WEIGHT'], aggfunc='sum', normalize='columns', margins=True)
    freq.rename(columns={"All": var},inplace=True)
    freq = freq[var]
    print(title)
    print(freq)
    print()
    print(title)
    priorities = pd.crosstab(df[var], df['Q2'], values=df['WEIGHT'], aggfunc='sum', normalize='columns', margins=True)
    print(priorities)
    priorities.to_excel(writer, sheet_name=str(var), index=True)

tab_list = ['Q7', 'Q8', 'Q9']
for x in tab_list:
    # crosser(all_df, x, all_writer, 'ALL')
    crosser(young_df, x, young_writer, 'YOUNG')
    crosser(old_df, x, old_writer, 'OLD')
    # crosser(closed, x, old_writer)
    # crosser(opened, x, old_writer)

all_writer.save()
young_writer.save()
old_writer.save()
closed_writer.save()
opened_writer.save()

sys.exit()

