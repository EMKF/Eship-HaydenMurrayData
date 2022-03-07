# data was downloaded from: https://www.federalreserve.gov/consumerscommunities/shed_data.htm

import pandas as pd
import numpy as np
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

def data_create():
    # download covid-SHED data from url
    z = urlopen('https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2019_supplemental_survey_sept_2020_(CSV).zip')
    myzip = ZipFile(BytesIO(z.read())).extract('publicJuly2020.csv')
    df = pd.read_csv(myzip)
    # subset by columns of interest
    df = df[df.columns[pd.Series(df.columns).str.startswith(('caseid2019', 'weight', 'B2', 'EF', 'CV'))]]
    print(df.head(100))
    sys.exit()
    # replace the refused with NaNs
    df.replace('Refused', np.nan, inplace=True)
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    dir = '/Users/hmurray/Desktop/data/SHED/covid_shed/python_outputs/covid_SHED_ctabs.xlsx'
    writer = pd.ExcelWriter(dir, engine='xlsxwriter')
    return df


if __name__ == '__main__':
    df = data_create()



# create list of column names
freq = pd.DataFrame()
ctabs = pd.DataFrame()
output = pd.DataFrame()
def ctabber(var):
    print()
    # frequencies
    freq = df.groupby(var)['weight'].sum().reset_index()
    freq['percent'] = freq['weight'] / df['weight'].sum()
    freq.rename(columns={"weight": "count"}, inplace=True)

    # cross tabs
    ctabs = pd.crosstab(df[var], df['CV1'], values=df['weight'], aggfunc='sum', normalize='columns')

    # merge frequencies and crosstabs
    output = freq.merge(ctabs, on=var)
    print(output)

    # export to excel
    output.to_excel(writer, sheet_name=str(var), index=False)

# create list of vars to analyze
var_list = df[df.columns[pd.Series(df.columns).str.startswith(('B2', 'EF', 'CV'))]]

# loop over list of relevant variables and pass each through frequency and cross tab function
for x in var_list:
    ctabber(x)

# save the excel writer and exit
writer.save()
sys.exit()