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

# state level populations 2005-2010
state05_10 = pd.DataFrame([])
for num in range(7,13):
    data = 'https://api.census.gov/data/2000/pep/int_population?get=GEONAME,POP,DATE_DESC&for=state:*&DATE_={num}&key=4530f6af9e686fe2f12b443f4c7d9246ffbc503e'.format(num=num)
    response = requests.get(data).json()
    df = pd.DataFrame(response[1:], columns=response[0])
    state05_10 = state05_10.append(df, ignore_index=True)
print(state05_10)

# us level populations 2005-2010
us = pd.DataFrame([])
for num in range(7,13):
    data = 'https://api.census.gov/data/2000/pep/int_population?get=GEONAME,POP,DATE_DESC&for=us:1&DATE_={num}&key=4530f6af9e686fe2f12b443f4c7d9246ffbc503e'.format(num=num)
    response = requests.get(data).json()
    df = pd.DataFrame(response[1:], columns=response[0])
    us = us.append(df, ignore_index=True)
print(us)

# state level populations 2011-2018
# THIS IS PULLING 2018. NEED TO LOOP OVER PARAMETERS TO PULL IN RANGE OF YEARS
# THIS IS PULLING 2018. NEED TO LOOP OVER PARAMETERS TO PULL IN RANGE OF YEARS
# THIS IS PULLING 2018. NEED TO LOOP OVER PARAMETERS TO PULL IN RANGE OF YEARS
state18 = pd.DataFrame([])
for num in range(4,5):
    data = 'https://api.census.gov/data/2018/pep/population?get=GEONAME,POP,DATE_DESC&for=state:*&key=4530f6af9e686fe2f12b443f4c7d9246ffbc503e'.format(num=num)
    response = requests.get(data).json()
    df = pd.DataFrame(response[1:], columns=response[0])
    state18 = state18.append(df, ignore_index=True)
print(state18)
sys.exit()











