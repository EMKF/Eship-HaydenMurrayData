# data pulled from: https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html#:~:text=Each%20year%2C%20the%20Census%20Bureau's,of%20change%2C%20and%20housing%20units.
# state fips: http://code.activestate.com/recipes/577775-state-fips-codes-dict/

import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
import seaborn as sns
from textwrap import wrap
from pandas.io.json import json_normalize
import sys
import io

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull from API
r = requests.get('https://api.census.gov/data/2019/pep/population?get=POP&for=state:*&key=4530f6af9e686fe2f12b443f4c7d9246ffbc503e')
j = r.json()
df = pd.DataFrame(j, columns=j.pop(0))

# recode state_codes
state_codes = {
    'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
    'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
    'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
    'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
    'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
    'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
    'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
    'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
    'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46'
}

# recode to state strings
inv_state_codes = {v: k for k, v in state_codes.items()}
df["state"].replace(inv_state_codes, inplace=True)
print(df)