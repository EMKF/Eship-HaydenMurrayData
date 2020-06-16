# data was downloaded from: https://www.federalreserve.gov/consumerscommunities/shed_data.htm

import pandas as pd
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None


# download covid-SHED data from url
z = urlopen('https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2019_supplemental_survey_april_2020_(CSV).zip')
myzip = ZipFile(BytesIO(z.read())).extract('publicApril2020.csv')
df = pd.read_csv(myzip)
print(df.head())

# Create a Pandas Excel writer using XlsxWriter as the engine.
dir = '/Users/hmurray/Desktop/data/SHED/covid_shed/python_outputs/covid_SHED_ctabs.xlsx'
writer = pd.ExcelWriter(dir, engine='xlsxwriter')

# create list of column names
freq = pd.DataFrame()
ctabs = pd.DataFrame()
output = pd.DataFrame()
def ctabber(var):
    # frequencies
    print()
    freq = df.groupby(var)['weight'].sum().reset_index()
    freq['percent'] = freq['weight'] / df['weight'].sum()
    freq.rename(columns={"weight": "count"}, inplace=True)
    # print(freq)
    print()
    # cross tabs
    ctabs = pd.crosstab(df[var], df['CV1'], values=df['weight'], aggfunc='sum', normalize='columns', margins=True)
    # print(ctabs)
    print()
    output = freq.merge(ctabs, on=var)
    print(output)
    ctabs.to_excel(writer, sheet_name=str(var), index=True)

# create list of vars to analyze
var_list = df[df.columns[pd.Series(df.columns).str.startswith(('B2', 'EF'))]]

# loop over list of relevant variables and pass each through frequency and cross tab function
for x in var_list:
    ctabber(x)

# save the excel writer and exit
writer.save()
sys.exit()