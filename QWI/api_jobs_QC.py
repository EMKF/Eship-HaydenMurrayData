# data obtained from https://ledextract.ces.census.gov/static/data.html
# unemployment rate from BLS series number LNS14000000: https://data.bls.gov/timeseries/LNS14000000

import pandas as pd
import sys
import requests
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.f' % x)
pd.options.mode.chained_assignment = None

key = '4530f6af9e686fe2f12b443f4c7d9246ffbc503e'

contribution = pd.DataFrame()
for x in range(2004, 2018):
    data = 'https://api.census.gov/data/timeseries/qwi/rh?get=Emp&for=state:01,02&time={x}&key=4530f6af9e686fe2f12b443f4c7d9246ffbc503e'.format(x=x)
    response = requests.get(data).json()
    df = pd.DataFrame(response[1:], columns=response[0])
    df = pd.DataFrame(response[1:], columns=response[0])
    contribution = contribution.append(df, ignore_index=True)


contribution['time'] = contribution['time'].astype(str).str[:-3].astype(np.int64)
print(contribution.head(10))


# contribution: EMP(year, region, all age categories) / EMP(year, region, specific age categories)


# state_abb_fips_codes_dic = {
#     'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
#     'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
#     'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
#     'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
#     'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
#     'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
#     'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
#     'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
#     'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46'
# }
#
# state_abb_state_names_dic = {
#         'AK': 'Alaska',
#         'AL': 'Alabama',
#         'AR': 'Arkansas',
#         'AZ': 'Arizona',
#         'CA': 'California',
#         'CO': 'Colorado',
#         'CT': 'Connecticut',
#         'DC': 'District of Columbia',
#         'DE': 'Delaware',
#         'FL': 'Florida',
#         'GA': 'Georgia',
#         'HI': 'Hawaii',
#         'IA': 'Iowa',
#         'ID': 'Idaho',
#         'IL': 'Illinois',
#         'IN': 'Indiana',
#         'KS': 'Kansas',
#         'KY': 'Kentucky',
#         'LA': 'Louisiana',
#         'MA': 'Massachusetts',
#         'MD': 'Maryland',
#         'ME': 'Maine',
#         'MI': 'Michigan',
#         'MN': 'Minnesota',
#         'MO': 'Missouri',
#         'MS': 'Mississippi',
#         'MT': 'Montana',
#         'NC': 'North Carolina',
#         'ND': 'North Dakota',
#         'NE': 'Nebraska',
#         'NH': 'New Hampshire',
#         'NJ': 'New Jersey',
#         'NM': 'New Mexico',
#         'NV': 'Nevada',
#         'NY': 'New York',
#         'OH': 'Ohio',
#         'OK': 'Oklahoma',
#         'OR': 'Oregon',
#         'PA': 'Pennsylvania',
#         'RI': 'Rhode Island',
#         'SC': 'South Carolina',
#         'SD': 'South Dakota',
#         'TN': 'Tennessee',
#         'TX': 'Texas',
#         'UT': 'Utah',
#         'VA': 'Virginia',
#         'VT': 'Vermont',
#         'WA': 'Washington',
#         'WI': 'Wisconsin',
#         'WV': 'West Virginia',
#         'WY': 'Wyoming'