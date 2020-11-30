# Data downloaded from: https://portal.census.gov/pulse/data/#downloads

import pandas as pd
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull data for first 5 weeks
dates1 = {'1': '26Apr20_2May20', '2': '3May20_9May20', '3': '10May20_16May20', '4': '17May20_23May20', '5': '24May20_30May20'}
pulse = pd.DataFrame()
for key, value in dates1.items():
    df = pd.read_excel('https://portal.census.gov/pulse/data/downloads/' + str(key) + '/national_sector_' + str(value) + '.xls', na_values='-')
    df.rename(columns={'NAICS_SECTOR': 'NAICS2'}, inplace=True)
    df = df[pd.isnull(df['NAICS2'])].reset_index(drop=True)
    df['WEEK'] = value
    df["ID"] = df["INSTRUMENT_ID"].astype(str) + ' - ' + df["ANSWER_ID"].astype(float).astype(str)
    pulse = pulse.append(df, sort=True).reset_index(drop=True)

# pull data for last 4 weeks
dates2 = {'6': '31May20_06Jun20', '7': '07Jun20_13Jun20', '8': '14Jun20_20Jun20', '9': '21Jun20_27Jun20'}
for key, value in dates2.items():
    df = pd.read_excel('https://portal.census.gov/pulse/data/downloads/' + str(key) + '/national_sector_' + str(value) + '.xls', na_values='-')
    df = df[pd.isnull(df['NAICS_SECTOR'])].reset_index(drop=True)
    df['WEEK'] = value
    df["ID"] = df["INSTRUMENT_ID"].astype(str) + ' - ' + df["ANSWER_ID"].astype(float).astype(str)
    pulse = pulse.append(df, sort=True).reset_index(drop=True)
print(pulse)

# pull codebook
code = pd.read_excel('https://portal.census.gov/pulse/data/downloads/codebook_5_17.xls')
code["ID"] = code["QUESTION_ID"].astype(str) + ' - ' + code["ANSWER_ID"].astype(str)

# combine question - answer code column and merge
df = pulse.merge(code, on='ID', how='left', indicator=True)

# convert the estimate percentage to a float so you can export in a clean way
df['ESTIMATE_PERCENTAGE'] = df['ESTIMATE_PERCENTAGE'].map(lambda x: x.rstrip('%'))
df['ESTIMATE_PERCENTAGE'] = df['ESTIMATE_PERCENTAGE'].astype(float)

# subset the dataframe
df = df[['WEEK', 'INSTRUMENT_ID', 'ID', 'QUESTION', 'ANSWER_TEXT', 'ESTIMATE_PERCENTAGE']]

# export xlsx for plots
df.to_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/python/small_bus_pulse/clean_bus_pulse_data.xlsx', index=False)

# create and export xlsx for
data = df.pivot_table(index=['INSTRUMENT_ID', 'QUESTION', 'ANSWER_TEXT'], columns='WEEK', values='ESTIMATE_PERCENTAGE').reset_index()
data.to_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/python/small_bus_pulse/long_clean_bus_pulse_data.xlsx', index=False)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/python/small_bus_pulse/tabbed_clean_bus_pulse_data.xlsx', engine='xlsxwriter')

# export each question to a different tab
book = {}
for q in df['INSTRUMENT_ID'].unique():
    book[q] = df[df['INSTRUMENT_ID'] == q]
    book[q] = book[q].pivot_table(index=['INSTRUMENT_ID', 'QUESTION', 'ANSWER_TEXT'], columns='WEEK', values='ESTIMATE_PERCENTAGE').reset_index()
    print(book[q])
    book[q].to_excel(writer, sheet_name=str(q), index=False)
writer.save()

sys.exit()