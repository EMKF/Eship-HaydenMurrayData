# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp90 and empc90 tells you employees in business in 1990

import pandas as pd
import time
import numpy as np
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# time
start = time.time()

# # pull from S3
employment = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Emp_SIC/NETS2017_Emp.txt',\
                 sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1', nrows=5000)

misc = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Misc/NETS2017_Misc.txt',\
                 sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1', nrows=5000)

# merge to get fips
df = employment.merge(misc, on='DunsNumber')

# create state_fip
df['hm_county_fips'] = df['FipsCounty'].astype(str).str.zfill(5)
df['state_fips'] = df['hm_county_fips'].astype(str).str[:2]
df.sort_values(by='state_fips', inplace=True)
df.reset_index(drop=True, inplace=True)

# state_codes dict, reverse dict, and recode fips to strings
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
df["state_fips"].replace(inv_state_codes, inplace=True)

# subset by column names we care about
df = df[['Emp05', 'Emp06', 'Emp07', 'Emp08', 'Emp09', 'Emp10',\
         'Emp11', 'Emp12', 'Emp13', 'Emp14', 'Emp15', 'Emp16',\
         'Emp17', 'DunsNumber', 'state_fips', 'FirstYear']]

# remove Emp and create the right year
df.columns = df.columns.str.replace('Emp', '')
df.columns = ['20' + col if col != 'DunsNumber' and col != 'state_fips' and col != 'FirstYear' else col for col in df.columns]
df.rename(columns={'2005': '2004', '2006': '2005', '2007': '2006', '2008': '2007', '2009': '2008',\
                   '2010': '2009', '2011': '2010', '2012': '2011', '2013': '2012', '2014': '2013',\
                   '2015': '2014', '2016': '2015', '2017': '2016'}, inplace=True)

# filter for firms that started in the relevant years
df = df[(df['FirstYear'] >= 2004)].reset_index(drop=True)

# add new column that is first year of hire
df['year_first_hire'] = df.fillna(method='bfill', axis=1).iloc[:, 0]
# df[cols].apply(lambda x: x.replace(np.nan, x.name + '_miss'))
print(df.head())


# calculate and print how long it took to run
end = time.time()
print((end/60) - (start/60))
sys.exit()

# pull bf8 data
bf8 = pd.read_csv('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/underlying_data_sent_to_danny/KESE_NEB_merge.csv',\
                   usecols=['state', 'year', 'bf8'])
print(bf8)
