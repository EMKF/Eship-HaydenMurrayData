# Data downloaded from: https://www.bls.gov/web/laus.supp.toc.htm
# link address: https://www.bls.gov/web/laus/ststdsadata.zip

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
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None


# writer
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/general_content/state_factsheet/unemployment_cleaner.xlsx', engine='xlsxwriter')

def data_create():
    # pull from s3
    df = pd.read_excel('/Users/hmurray/Desktop/data/general_content/state_factsheet/python_puller.xlsx', sheet_name='ststdsadata')
    print(df.head())
    df = df[['state', 'year', 'civ_non_inst_pop', 'labor_force',\
             'employment', 'unemployment']]
    return df

def feature_change(df):
    df = df.groupby(['state', 'year']).mean().reset_index()
    df['percent_labor'] = df['labor_force'] / df['civ_non_inst_pop']
    df['percent_emp'] = df['employment'] / df['labor_force']
    df['percent_unemp'] = df['unemployment'] / df['labor_force']
    df.to_excel(writer, sheet_name=str('yearly_emp'), index=False)

if __name__ == '__main__':
    df = data_create()
    df = feature_change(df)

writer.close()
sys.exit()