# data dowmloaded manually from https://factfinder.census.gov/bkmk/table/1.0/en/ASE/2016/0CSCBO08

import os
import sys
import time
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# load PEP data
df = pd.read_csv('/Users/hmurray/Desktop/data/ASE/ASE_edu/ASE_2016_00CSCBO07_with_ann.csv')
print(df.head())

