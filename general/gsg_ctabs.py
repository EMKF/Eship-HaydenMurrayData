# data was provided by Jessica on May 29th, 2020

import pandas as pd
import sys
import numpy as np
import quantipy as qp

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

# read in data
all_df = pd.read_csv('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/raw_gsg_6.3.csv')
young_df = all_df.loc[all_df['Q4']==1]
old_df = all_df.loc[all_df['Q4']!=1]
closed = all_df.loc[all_df['Q4']!=1]
opened = all_df.loc[all_df['Q4']!=1]
print(all_df.head())
print(young_df.head())
print(old_df.head())

# Create a Pandas Excel writer using XlsxWriter as the engine.
all_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/all_ctabs_priorities.xlsx', engine='xlsxwriter')
young_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/young_ctabs_priorities.xlsx', engine='xlsxwriter')
old_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/old_ctabs_priorities.xlsx', engine='xlsxwriter')

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
    priorities = pd.crosstab(df[var], df['Q2'], values=df['WEIGHT'], aggfunc='sum', normalize='columns', margins=True)
    print(priorities)
    priorities.to_excel(writer, sheet_name=str(var), index=True)

tab_list = ['Q2', 'Q7', 'Q8', 'Q9']
for x in tab_list:
    crosser(all_df, x, all_writer)
    crosser(young_df, x, young_writer)
    crosser(old_df, x, old_writer)

all_writer.save()
young_writer.save()
sys.exit()

