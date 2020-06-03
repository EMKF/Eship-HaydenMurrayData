# data was provided by Jessica on May 29th, 2020

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
df = pd.read_csv('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/raw_gsg_5.26.csv')
print(df.head())

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/ctabs_priorities.xlsx', engine='xlsxwriter')

# crosstabs
priorities = pd.DataFrame()
def crosser(var):
    print()
    print(df[var].value_counts(normalize=True))
    print()
    priorities = pd.crosstab(df[var], df['Q4'], normalize='columns').round(4)
    print(priorities)
    print()
    priorities.to_excel(writer, sheet_name=str(var), index=True)
    return priorities

tab_list = ['Q2', 'Q3', 'Q4', 'Q7', 'Q8', 'Q9', 'Q56_15_1', 'Q7']
for x in tab_list:
    crosser(x)


writer.save()
sys.exit()

sys.exit()