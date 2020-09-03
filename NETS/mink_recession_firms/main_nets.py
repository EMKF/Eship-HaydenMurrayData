# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp90 and empc90 tells you employees in business in 1990

import pandas as pd
import time
import numpy as np
import sys
import NETS.constants as c

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# time
start = time.time()

def data_create():
    # pull from s3
    return pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Misc/NETS2017_Misc.txt', \
                     sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1', nrows=5000)
    print(df.head())


def feature_change(df):
    df['hm_county_fips'] = df['FipsCounty'].astype(str).str.zfill(5)
    df['state_fips'] = df['hm_county_fips'].astype(str).str[:2]
    df.sort_values(by='state_fips', inplace=True)
    df.reset_index(drop=True, inplace=True)

    # state_codes dict, reverse dict, and recode fips to strings
    c.state_codes
    df["state_fips"].replace(c.inv_state_codes, inplace=True)
    return df

def data_out(df):
    df.to_excel('/Users/hmurray/Desktop/main_scratch.xlsx', index=False)

if __name__ == '__main__':
    df = data_create()
    df_temp = feature_change(df)
    data_out(df_temp)
    print(df.head())


sys.exit()

