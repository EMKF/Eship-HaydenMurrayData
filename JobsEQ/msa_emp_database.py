# data files sent to Hayden by Greg Chmura on June 16, 2020

import pandas as pd
import os
import sys
import requests
import numpy as np

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.f' % x)
pd.options.mode.chained_assignment = None

# US, state, AL counties, OK counties, UT counties,
df = pd.DataFrame()
for xlsx in os.listdir('/Users/hmurray/Desktop/data/jobsEQ/job_posts/emp_database/MSAs/'):
    print(xlsx)
    if xlsx != '.DS_Store':
        data = pd.read_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/emp_database/MSAs/' + str(xlsx), header=1)
        data = data[:-4]
        df = df.append(data, sort=False)


print(df.info())

df.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/emp_database/merged_MSAs/emp_merge_test.xlsx', index=False)
sys.exit()