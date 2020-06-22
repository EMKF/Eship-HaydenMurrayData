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
data = pd.read_csv('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/raw_gsg_6.3.csv')
tabs = pd.crosstab(data['Q4'], data['Q29'], values=data['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
print(tabs)
sys.exit()

# create new datasets to manipulate
data = data[['Q2', 'Q56_15_1', 'Q4', 'Q7', 'Q8', 'Q9', 'Q29', 'Q30', 'WEIGHT']]
data['NEW'] = data['Q4']
data['YOUNG'] = data['Q4']

# categorize Q4 (years in business) by NEW/NOT_NEW and YOUNG/MATURE
data["NEW"].replace({1: "NEW", 2: "NOT_NEW", 3: "NOT_NEW", 4: "NOT_NEW", 5: "NOT_NEW", 6: "NOT_NEW", 7: "NOT_NEW"}, inplace=True)
data['YOUNG'].replace({1: "YOUNG", 2: "YOUNG", 3: "YOUNG", 4: "YOUNG", 5: "YOUNG", 6: "MATURE", 7: "MATURE"}, inplace=True)

# rename Q2 and Q56_15_1
data['Q2'] = data['Q2'].astype(str).replace(str(1), 'Still in business').replace(str(2), 'It has closed')
data['Q56_15_1'] = data['Q56_15_1'].astype(str).replace(str(1), 'temp_closed').replace(str(0), 'did_not_close')

# create priority tab list and rename via for loop
structure_list = ['Q7', 'Q8', 'Q9']
for x in structure_list:
    data[x] = data[x].astype(str).replace(str(1), '1 Just myself and co-owners, no other employees').replace(str(2), '2 1-10')\
.replace(str(3), '3 11-50').replace(str(4), '4 51-100').replace(str(5), '5 More than 100')

# Create a Pandas Excel writer using XlsxWriter as the engine.
new_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/new_ctabs_priorities.xlsx', engine='xlsxwriter')
young_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/young_ctabs_priorities.xlsx', engine='xlsxwriter')
two_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/two_ctabs_priorities.xlsx', engine='xlsxwriter')

# prep crosstabs
freq = pd.DataFrame()
ctabs = pd.DataFrame()
def crosser(df, var):
    # weighted frequency distribution
    print()
    freq = pd.crosstab(df[var], df[var], values=df['WEIGHT'], aggfunc='sum', normalize='columns', margins=True)
    freq.rename(columns={"All": var},inplace=True)
    freq = freq[var]
    print(freq)
    print()

    # weighted crosstab closures
    two = pd.crosstab(df[var], df['Q56_15_1'], values=df['WEIGHT'], aggfunc='sum', normalize='columns', margins=True)
    print(two)
    two.to_excel(two_writer, sheet_name=str(var), index=True)
    print()

    # weighted crosstab new conditional on closures
    new = pd.crosstab(df['Q56_15_1'], [df['NEW'], df[var]], values=df['WEIGHT'], aggfunc='sum', normalize='columns')
    new = new.transpose().reset_index(drop=False)
    print(new)
    new.to_excel(new_writer, sheet_name=str(var), index=True)

    # weighted crosstab young conditional on closures
    young = pd.crosstab(df['Q56_15_1'], [df['YOUNG'], df[var]], values=df['WEIGHT'], aggfunc='sum', normalize='columns')
    young = young.transpose().reset_index(drop=False)
    print(young)
    # young.to_excel(young_writer, sheet_name=str(var), index=True)

tab_list = ['Q7', 'Q8', 'Q9', 'Q29', 'Q30']
for x in tab_list:
    crosser(data, x)

two_writer.save()
new_writer.save()
young_writer.save()

sys.exit()

