import pandas as pd
import matplotlib.pyplot as plt
import requests
import seaborn as ax
import numpy as np
import zipfile
import urlopen
from textwrap import wrap
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

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