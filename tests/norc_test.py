import pandas as pd
import sys
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None



def data_create():
    df = pd.read_stata('/Users/hmurray/Downloads/Logically_Imputed_KFS_Public_Data/Public_Use_LI_Wide.dta')
    # df.to_csv('/Users/hmurray/Desktop/data/EPOP/pre_test_data/s2157_client_12Jan22.csv', index=False)
    return df

if __name__ == '__main__':
    df = data_create()
    print(df.head())