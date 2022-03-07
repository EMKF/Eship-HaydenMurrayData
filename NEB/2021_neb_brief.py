import os
import pandas as pd
from kauffman.data import bfs, bds, pep
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('chained_assignment',None)

def kcr_lib_puller():
    df = bfs(series_lst=['BA_BA', 'BA_CBA', 'BA_WBA', 'BA_HBA', 'BF_SBF8Q', 'BF_DUR8Q'], obs_level='us', industry='00', seasonally_adj=True, annualize=False, march_shift=False)
    print(df.head())
    print(df.tail())
    df.to_excel('/Users/hmurray/Desktop/data/NEB/2021_neb_briefs/data/neb_brief_underlying_bfs_variables.xlsx')
    return df

def local_puller():
    df = pd.read_excel('/Users/hmurray/Desktop/data/NEB/2021_neb_briefs/data/neb_brief_underlying_bfs_variables.xlsx')
    return df

if __name__ == '__main__':
    # df = kcr_lib_puller()
    df = local_puller()
    print(df)