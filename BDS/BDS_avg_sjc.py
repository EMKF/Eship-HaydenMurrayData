# data obtained from Rob's email 4.27 @ 1:45pm

import os
import sys
import csv
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None


# pull data
df = pd.read_excel('/Users/hmurray/Desktop/data/BDS/average_jobs_per_startup/BDS_avg_sjc.xlsx')
df['avg_emp_new_firms'] = df['new_firms_employees']/df['new_firms']
df.to_excel('/Users/hmurray/Desktop/data/BDS/average_jobs_per_startup/average_jobs_per_startup.xlsx', index=False)
print(df)






