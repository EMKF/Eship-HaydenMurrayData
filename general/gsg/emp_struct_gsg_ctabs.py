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

# create new datasets to manipulate
data = data[['Q2', 'Q56_15_1', 'Q4', 'Q7', 'Q8', 'Q9', 'Q29', 'Q30', 'WEIGHT']]

# calculate correlations between employee structure variables
print(data['Q7'].corr(data['Q8']))
print(data['Q7'].corr(data['Q9']))
print(data['Q8'].corr(data['Q9']))

# categorize Q4 (years in business) by NEW/YOUNG/MATURE
data["Q4"].replace({1: "NEW", 2: "YOUNG", 3: "YOUNG", 4: "YOUNG", 5: "YOUNG", 6: "MATURE", 7: "MATURE"}, inplace=True)
data['AGE'] = data['Q4']

# rename Q2 and Q56_15_1
data['Q2'] = data['Q2'].astype(str).replace(str(1), 'Still in business').replace(str(2), 'It has closed')
data['Q56_15_1'] = data['Q56_15_1'].astype(str).replace(str(1), 'temp_closed').replace(str(0), 'did_not_close')

# recreate employee structure categories
data['full_time'] = data['Q7']
data['part_time'] = data['Q8']
data['contract'] = data['Q9']
structure_list = ['full_time', 'part_time', 'contract']
for x in structure_list:
    data[x] = data[x].astype(str).replace(str(1), '1 Just myself and co-owners, no other employees').replace(str(2), '2 1-10')\
.replace(str(3), '3-5 10+').replace(str(4), '3-5 10+').replace(str(5), '3-5 10+')

# Create a Pandas Excel writer using XlsxWriter as the engine.
freq_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/freq_priorities.xlsx', engine='xlsxwriter')
two_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/two_ctabs_priorities.xlsx', engine='xlsxwriter')
three_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/three_ctabs_priorities.xlsx', engine='xlsxwriter')

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
    freq.to_excel(freq_writer, sheet_name=str(var), index=True)
    print()

    # weighted crosstab closures
    two = pd.crosstab(df[var], df['Q56_15_1'], values=df['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
    print(two)
    two.to_excel(two_writer, sheet_name=str(var), index=True)
    print()

    # weighted crosstab new conditional on closures
    new = pd.crosstab(df['Q56_15_1'], [df['AGE'], df[var]], values=df['WEIGHT'], aggfunc='sum', normalize='columns')
    new = new.transpose().reset_index(drop=False)
    print(new)
    new.to_excel(three_writer, sheet_name=str(var), index=True)


tab_list = ['Q4', 'Q56_15_1', 'full_time', 'part_time', 'contract']
for x in tab_list:
    crosser(data, x)

freq_writer.save()
two_writer.save()
three_writer.save()

# emp structure logic check analysis writer
full_part_cont_writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/jessica/data/full_part_cont_writer.xlsx', engine='xlsxwriter')

# emp structure logic check analysis
print()
full_part = pd.crosstab(data['full_time'], data['part_time'], values=data['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
print(full_part)
full_part.to_excel(full_part_cont_writer, sheet_name='full_part', index=True)


print()
full_contract = pd.crosstab(data['full_time'], data['contract'], values=data['WEIGHT'], aggfunc='sum', normalize='index', margins=True)
print(full_contract)
full_contract.to_excel(full_part_cont_writer, sheet_name='full_contract', index=True)


full_part_cont_writer.save()
sys.exit()

