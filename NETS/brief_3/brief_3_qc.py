# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp90 and empc90 tells you employees in business in 1990

import pandas as pd
import numpy as np
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull bf8 data
bf8 = pd.read_csv('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/underlying_data_sent_to_danny/KESE_NEB_merge.csv',\
                   usecols=['state', 'year', 'bf8'])
print(bf8)

# pull in nets data
nets = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Emp_SIC/NETS2017_Emp.txt',\
                 sep='\t', na_values=' ', lineterminator='\r', nrows=500, error_bad_lines=False, encoding='latin1')
print(nets)

# subtract 1 from each emp to subtract for owners
# +1 to year e.g. emp92 is employment for 1993


# # check and export to excel
# df.to_excel('/Users/hmurray/Desktop/data/NETS/bf8_nets_forms_qc.xlsx', index=False)