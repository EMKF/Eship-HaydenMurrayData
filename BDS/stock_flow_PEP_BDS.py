# data downloaded manually from https://www2.census.gov/programs-surveys/popest/datasets/2010-2019/national/totals/nst-est2019-popchg2010_2019.csv

import os
import sys
import time
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import joblib
import constants as c
import io
import json

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)



# pull data from Census API
base_url = 'https://api.census.gov/data/2000/pep/int_population'
key = '4530f6af9e686fe2f12b443f4c7d9246ffbc503e'



data = 'https://api.census.gov/data/2000/pep/int_population?get=GEONAME,POP,DATE_DESC&for=state:*&DATE_=1&key=4530f6af9e686fe2f12b443f4c7d9246ffbc503e'
response = requests.get(data).json()
print(response)
df = pd.DataFrame(response[1:], columns=response[0])
print(df)



# #store the response in a dataframe
# laZipPopulations = pd.DataFrame(columns=['zipcode', 'population'], data=formattedResponse)
#
# #save that dataframe to a CSV spreadsheet
# laZipPopulations.to_csv('laZipPopulations.csv', index=False)

#
# # load 2010-2019 PEP data
# pep10 = pd.read_csv('/Users/hmurray/Desktop/data/PEP/state_national_estimates/nst-est2019-popchg2010_2019.csv')
# pep10 = pep10[(pep10['SUMLEV'] == 10) | (pep10['SUMLEV'] == 40)]
# pep10.columns = pep10.columns.str.replace("POPESTIMATE", "")
# print(pep10)
#
#
#
# # load 2000 - 2010 PEP data
# pep00 = pd.read_csv('/Users/hmurray/Desktop/data/PEP/state_national_estimates/st-est00int-alldata.csv')
# print(pep00)