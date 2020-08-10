# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp90 and empc90 tells you

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

# # # pull from S3
# df = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Emp_SIC/NETS2017_Emp.txt',\
#                  sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1')

df = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Emp_SIC/NETS2017_Emp.txt',\
                 sep='\t', na_values=' ', lineterminator='\r', nrows=500, error_bad_lines=False, encoding='latin1', low_memory=False)

# check and export to excel
print(df.head(500))
df.to_excel('/Users/hmurray/Desktop/data/NETS/ba_emp_qc.xlsx', index=False)

sys.exit()


#########################################################################################################################
################################################# Danny's Files #########################################################
#########################################################################################################################

# pull in data
df = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_2/qc/db_2_raw.xlsx', sheet_name='all_years',\
                   usecols=['state', 'year', 'ba', 'emp', 'emp_no_owners', 'ratio_emp_bf'])

# recalculate ratio
df['ratio_qc'] = df['emp_no_owners'] / df['ba']
print(df.head())
sys.exit()
# figure_1
figure_1 = df.groupby(df['year'])[['ba', 'nets_new_establishments']].median().reset_index()
print(figure_1)
# plot figure_1
figure_1.plot(x='year', y=['ba', 'nets_new_establishments'])
plt.xticks(rotation=45)
plt.title("\n".join(wrap('Figure 1: Median Ratio of New Hires to Business Formations Over Time, 2005-2016', 50)))
plt.tight_layout()
plt.grid()
plt.savefig('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/qc/figure_1.png')
plt.show()