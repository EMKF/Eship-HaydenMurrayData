import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/Maddi_Oldstone/MO_Data_Briefs/ASE_Reasons_Own_Business/ASE_Reasons_Own_Bus.csv'
                 ,header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# condense dataframe
df = df[['GEO.display-label','ASECBO.display-label','YIBSZFI.display-label','REASONOWN.display-label','OWNPDEMP_PCT']]
print(df.head())


