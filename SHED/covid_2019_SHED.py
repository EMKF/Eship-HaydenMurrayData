# data was downloaded from:

import pandas as pd
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
import dload
import os
import sys
import requests
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None


# covid_shed = pd.read_csv('/Users/hmurray/Desktop/data/SHED/covid_shed/publicApril2020.csv')
# print(covid_shed.info())

z = urlopen('https://www.federalreserve.gov/consumerscommunities/files/SHED_public_use_data_2019_supplemental_survey_april_2020_(CSV).zip')
myzip = ZipFile(BytesIO(z.read())).extract('publicApril2020.csv')
df = pd.read_csv(myzip)
print(df.head())

sys.exit()