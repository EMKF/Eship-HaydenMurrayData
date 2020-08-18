# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp91 and empc91 tells you employees in business in 1990

import pandas as pd
import numpy as np
import time
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
                 sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1')

misc = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Misc/NETS2017_Misc.txt',\
                 sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1')

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

# sum employment by year
def summer(col):
    emps = df.groupby(['state_fips'])[col].sum()
    return emps

# define years
years = ('Emp05', 'Emp06', 'Emp07', 'Emp08', 'Emp09', 'Emp10', 'Emp11', 'Emp12', 'Emp13', 'Emp14', 'Emp15', 'Emp16', 'Emp17')

# create empty df, loop over year columns, and append
data = pd.DataFrame()
for col in years:
    data = data.append(summer(col), sort=False)

# manipulate output of employment sum function
data = data.reset_index()
data['index'] = data['index'].str.replace('Emp', '')
data['index'] = '20' + data['index'].astype(str)
data['index'] = data['index'].astype(int) - 1
data = data.set_index('index').transpose().reset_index()
data.rename(columns={"index": "state"}, inplace=True)

# melt so we can easily merge
data = pd.melt(data, id_vars =['state'], value_vars = (range(2004, 2017)), var_name ='year', value_name ='nets_employment')

# pull business applications data
ba = pd.read_csv('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/underlying_data_sent_to_danny/KESE_NEB_merge.csv',\
                   usecols=['state', 'year', 'ba'])

# merge ba and nets employment
final = pd.merge(ba, data, on=['state', 'year'])

# calculate the emp per estab ratio
final['ratio_estab_ba'] = final['ba'] / final['nets_employment']
print(final)

# check how long it takes to run
end = time.time()
print((end/60) - (start/60))
sys.exit()







sys.exit()

# # check and export to excel
# df.to_excel('/Users/hmurray/Desktop/data/NETS/ba_emp_qc.xlsx', index=False)

#########################################################################################################################
################################################# Danny's Files #########################################################
#########################################################################################################################

# pull in data
df = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_2/qc/db_2_raw.xlsx', sheet_name='all_years',\
                   usecols=['state', 'year', 'ba', 'emp', 'emp_no_owners', 'ratio_emp_bf'])

# recalculate ratio
df['ratio_qc'] = df['emp_no_owners'] / df['ba']
print(df.head())
sys.exit()
# figure_1
figure_1 = df.groupby(df['year'])[['ba', 'nets_new_establishments']].median().reset_index()
print(figure_1)
# plot figure_1
figure_1.plot(x='year', y=['ba', 'nets_new_establishments'])
plt.xticks(rotation=45)
plt.title("\n".join(wrap('Figure 1: Median Ratio of New Hires to Business Formations Over Time, 2005-2016', 50)))
plt.tight_layout()
plt.grid()
plt.savefig('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/qc/figure_1.png')
plt.show()