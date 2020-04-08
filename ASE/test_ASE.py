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



df = pd.read_csv('/Users/hmurray/Downloads/SE1600CSCB32.dat', sep='|', low_memory=False)
print(df.head(100))
df.to_excel('/Users/hmurray/Desktop/data/ASE/dta_pulls/regulations_business_profitability.xlsx', index=False)

