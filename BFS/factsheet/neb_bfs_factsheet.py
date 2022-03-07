# data downloaded from csv link at the bottom of this webpage: https://www.census.gov/econ/bfs/data.html
# csv link: https://www.census.gov/econ/bfs/csv/bfs_quarterly.csv
# pulling from Kauffman library

import sys
import pandas as pd
from kauffman.data import bfs


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# read in ba and wba
def data_create():
    # pull from kauffman library
    df = bfs(['BA_BA', 'BA_CBA', 'BA_HBA', 'BA_WBA', 'BF_BF4Q', 'BF_BF8Q', 'BF_PBF4Q',\
              'BF_PBF8Q', 'BF_SBF4Q', 'BF_SBF8Q', 'BF_DUR4Q', 'BF_DUR8Q'],\
             obs_level='us', industry='all', annualize=False)
    # df = bfs(['BA_BA'],\
    #          obs_level='us', industry='all', annualize=True)

    # calculate percent BA_WBA and percent BA_CBA
    df['percent_wba'] = df['BA_WBA'] / df['BA_BA']
    df['percent_cba'] = df['BA_CBA'] / df['BA_BA']
    df['percent_SBF8Q'] = df['BF_SBF8Q'] / df['BA_BA']
    print(df.head())
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    location = '/Users/hmurray/Desktop/data/NEB/factsheet/neb_factsheet_data.xlsx'
    writer = pd.ExcelWriter(location, engine='xlsxwriter')

    # export each df to sepeerate sheet
    df.to_excel(writer, sheet_name='bfs', index=False)

    # save to excel
    writer.save()
    return df



if __name__ == '__main__':
    df = data_create()

sys.exit()