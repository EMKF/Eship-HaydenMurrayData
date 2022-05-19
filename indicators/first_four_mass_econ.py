import sys
import pandas as pd
import kauffman.data as kauffman
import matplotlib.pyplot as plt
import datetime
import numpy as np
from textwrap import wrap
from matplotlib.dates import date2num

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    # pull 2021 neb data download
    df = pd.read_excel('/Users/hmurray/Desktop/data/BFS/indicators/ME_KFN_BFS_MetroNonMetro_DataSummary_vShare_032322.xlsx',
                       sheet_name='BFS_Annual_Combo_20052020',
                       skiprows=7,
                       usecols=lambda x: 'Unnamed' not in x)
    print(df.head())
    return df

if __name__ == '__main__':
    df = data_create()