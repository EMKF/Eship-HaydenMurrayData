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

def data_in()
df = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/ASE_2016_reasons_own_business.csv')
print(df.head())


