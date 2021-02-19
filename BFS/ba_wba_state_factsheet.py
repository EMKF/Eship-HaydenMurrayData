# data downloaded from csv link at the bottom of this webpage: https://www.census.gov/econ/bfs/data.html
# pulling from Kauffman library

import sys
import pandas as pd
import kauffman


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# read in ba and wba
def data_create():
    # # pull ba and wba
    # df = pd.read_csv('https://www.census.gov/econ/bfs/csv/bfs_quarterly.csv')

    # pull from kauffman library
    df = kauffman.bfs(['BA_BA', 'BA_WBA'], 'state', annualize=True)
    print(df)
    df = df.groupby(['fips', 'region', 'time']).sum(min_count=12)
    print(df)
    # df = df.groupby(df['time'])
    # print(df.head())
    sys.exit()
    # convert columns to int
    df["Q1"] = df["Q1"].str.extract('(\d+)', expand=False)
    df["Q2"] = df["Q2"].str.extract('(\d+)', expand=False)
    df["Q3"] = df["Q3"].str.extract('(\d+)', expand=False)
    df["Q4"] = df["Q4"].str.extract('(\d+)', expand=False)
    df["Q1"] = pd.to_numeric(df["Q1"])
    df["Q2"] = pd.to_numeric(df["Q2"])
    df["Q3"] = pd.to_numeric(df["Q3"])
    df["Q4"] = pd.to_numeric(df["Q4"])

    # sum quarterly data
    df['annual_sum'] = df['Q1'] + df['Q2'] + df['Q3'] + df['Q4']

    # groupby year
    df = df.groupby(df['year'])
    df = pd.DataFrame()
    # collapse df
    df = df['series', 'geo', 'year', 'annual_sum']

    # pivot
    df = df.pivot_table(index=['geo', 'year'], columns='series')
    print(df.head())
    sys.exit()

    # merge ba and pep
    df['percent_wba'] = df['BA_WBA'] / df['BA_BA']
    print(df.head())

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    location = '/Users/hmurray/Desktop/data/general_content/state_factsheet/data/bfs_applications.xlsx'
    writer = pd.ExcelWriter(location, engine='xlsxwriter')

    # export each df to sepeerate sheet
    df.to_excel(writer, sheet_name='ba_and_wba', index=False)

    # save to excel
    writer.save()
    return df



if __name__ == '__main__':
    df = data_create()

sys.exit()