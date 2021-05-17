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
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# read in ba and wba
def data_create():
    # download covid-SHED data from url
    z = urlopen('https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2019_(CSV).zip')

    myzip = ZipFile(BytesIO(z.read())).extract('publicJuly2020.csv')
    shed_year = pd.read_csv(myzip)
    df = pd.DataFrame()
    df = df.append(shed_year, ignore_index=True)
    print(df.head())
    return df


if __name__ == '__main__':
    df = data_create()
    # df = plotter_1(df)

sys.exit()