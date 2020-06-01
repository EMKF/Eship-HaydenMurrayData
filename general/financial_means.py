import pandas as pd
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull raw data
raw = pd.read_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/python/small_bus_pulse/national_sector_17May20_23May20.xls', na_values='-')
raw = raw[pd.isnull(raw['NAICS2'])]
raw["ID"] = raw["INSTRUMENT_ID"].astype(str) + ' - ' + raw["ANSWER_ID"].astype(float).astype(str)

# pull codebook
code = pd.read_excel('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/python/small_bus_pulse/codebook.xls')
code["ID"] = code["INSTRUMENT_ID"].astype(str) + ' - ' + code["ANSWER_ID"].astype(str)

# combine question - answer code column and merge
df = raw.merge(code, on='ID', how='left', indicator=True)
df = df[['INSTRUMENT_ID_y', 'QUESTION_TEXT', 'ANSWER_TEXT', 'ESTIMATE_PERCENTAGE']]
df.rename(columns={"INSTRUMENT_ID_y": "QUESTION_ID"},inplace=True)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/covid_bus_pulse_SHED_fin_means/python/small_bus_pulse/clean_survey_data.xlsx', engine='xlsxwriter')

# unstack reasons
book = {}
for q in df['QUESTION_ID'].unique():
    book[q] = df[df['QUESTION_ID'] == q]
    print(book[q].head())
    book[q].to_excel(writer, sheet_name=str(q), index=False)

writer.save()
sys.exit()


