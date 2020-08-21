# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp90 and empc90 tells you employees in business in 1990

import pandas as pd
import time
import sys
pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

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
inv_state_codes = {v: k for k, v in state_codes.items()}
start = time.time()
pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Misc/NETS2017_Misc.txt', sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1'). \
    query('FipsCounty == FipsCounty').\
    assign(
        fips=lambda x: x['FipsCounty'].astype(int).astype(str).str.zfill(5),
        state_fips=lambda x: x['fips'].str[:2].map(inv_state_codes)
    ) \
    [['DunsNumber', 'state_fips', 'FirstYear']].\
    groupby(['state_fips', 'FirstYear']).count().\
    reset_index().\
    rename(columns={'DunsNumber': 'est_count'}).\
    to_csv('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/st_est_counts.csv', index=False)
print((time.time() / 60) - (start / 60))


sys.exit()




